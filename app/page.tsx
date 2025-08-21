"use server"

import { SignInButton } from "@/components/buttons/sign-in-button";
import { auth } from "@/auth";
import Link from "next/link";
import { SignOutButton } from "@/components/buttons/sign-out-button";
import styles from "./page.module.css";

export default async function Home() {
  const session = await auth();

  if (session?.user) {
    return (
      <div className={styles.container}>
        <div className={styles.welcomeCard}>
          <div className={styles.userInfo}>
            {session.user.image && (
              <img 
                src={session.user.image} 
                alt={session.user.name || 'User'} 
                className={styles.userAvatar}
              />
            )}
            <h2 className={styles.userName}>{session.user.name}</h2>
            <p className={styles.userEmail}>{session.user.email}</p>
          </div>
          
          <div className={styles.buttonGroup}>
            <Link href="/user-info" className={styles.link}>
              View User Info
            </Link>
            <SignOutButton />
          </div>
        </div>
      </div>
    )
  }

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
        
        <form className={styles.signInForm}>
          <div className={styles.formGroup}>
            <label htmlFor="email" className={styles.label}>Email</label>
            <input 
              type="email" 
              id="email"
              placeholder="Enter your email" 
              className={styles.input}
              required
            />
          </div>
          
          <div className={styles.formGroup}>
            <label htmlFor="password" className={styles.label}>Password</label>
            <input 
              type="password" 
              id="password"
              placeholder="Enter your password" 
              className={styles.input}
              required
            />
          </div>
          
          <div className={styles.formOptions}>
            <label className={styles.checkboxLabel}>
              <input type="checkbox" className={styles.checkbox} />
              <span className={styles.checkboxText}>Remember me</span>
            </label>
            <Link href="/forgot-password" className={styles.forgotLink}>
              Forgot password?
            </Link>
          </div>
          
          <button type="submit" className={styles.submitButton}>
            Sign In
          </button>
        </form>
        
        <p className={styles.signupText}>
          Don't have an account? <Link href="/signup" className={styles.signupLink}>Sign up</Link>
        </p>
      </div>
    </div>
  )
}