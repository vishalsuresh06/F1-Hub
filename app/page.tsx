"use server"

import { SignInButton } from "@/components/buttons/sign-in-button";
import Link from "next/link";
import styles from "./page.module.css";

export default async function Home() {
  return (
    <div className={styles.container}>
      <div className={styles.welcomeCard}>
        <h1 className={styles.welcomeTitle}>Welcome to Race Predictor</h1>
        <p className={styles.welcomeSubtitle}>
          Sign in with your GitHub account to get started
        </p>
        <SignInButton />
        <div className={styles.separator}>
          <hr className={styles.br}/>
          <p> OR </p>
          <hr className={styles.br}/>
        </div>

        <div className={styles.authLinks}>
          <Link href="/sign-in" className={styles.authLink}>
            Sign In with Email
          </Link>
          <p className={styles.signupText}>
            Don't have an account? <Link href="/signup" className={styles.signupLink}>Sign up</Link>
          </p>
        </div>
      </div>
    </div>
  )
}