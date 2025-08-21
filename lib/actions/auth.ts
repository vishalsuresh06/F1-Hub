"use server"

import { signIn, signOut } from "@/auth"
import { PrismaClient } from "../generated/prisma"
import bcrypt from "bcryptjs"
import { redirect } from "next/navigation"

const prisma = new PrismaClient()

export const login = async () => {
    await signIn("github", { redirectTo: "/"});
}

export const logout = async () => {
    await signOut({ redirectTo: "/"});
}

export const signUp = async (formData: FormData) => {
    const firstName = formData.get("firstName") as string
    const lastName = formData.get("lastName") as string
    const email = formData.get("email") as string
    const password = formData.get("password") as string
    const confirmPassword = formData.get("confirmPassword") as string
    const favTeam = formData.get("favTeam") as string || null
    const favDriver = formData.get("favDriver") as string || null

    // Validation
    if (!firstName || !lastName || !email || !password || !confirmPassword) {
        throw new Error("All required fields must be filled")
    }

    if (password !== confirmPassword) {
        throw new Error("Passwords do not match")
    }

    if (password.length < 6) {
        throw new Error("Password must be at least 6 characters long")
    }

    // Check if user already exists
    const existingUser = await prisma.user.findUnique({
        where: { email }
    })

    if (existingUser) {
        throw new Error("User with this email already exists")
    }

    // Hash password
    const hashedPassword = await bcrypt.hash(password, 12)

    // Create user
    const user = await prisma.user.create({
        data: {
            first_name: firstName,
            last_name: lastName,
            email,
            password: hashedPassword,
            fav_team: favTeam,
            fav_driver: favDriver
        }
    })

    // Redirect to sign-in page after successful registration
    redirect("/sign-in?message=Account created successfully! Please sign in.")
}
