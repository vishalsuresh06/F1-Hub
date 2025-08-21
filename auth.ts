import NextAuth from "next-auth";
import Credentials from "next-auth/providers/credentials";
import GitHub from "next-auth/providers/github";
import { validateAccount } from "./utils/account-validation";

interface User {
  id: string;
  email: string;
  name: string;
  password: string;
}

export const { auth, handlers, signIn, signOut } = NextAuth({
  providers: [
    GitHub,],
});
