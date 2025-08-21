"use client";

import React, { useState } from "react";
import styles from "../shared/form.module.css";
import Link from "next/link";
import { signUp } from "@/lib/actions/auth";

const SignUpForm = () => {
  const [error, setError] = useState<string | null>(null);
  const [isLoading, setIsLoading] = useState(false);

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    setError(null);
    setIsLoading(true);

    try {
      const formData = new FormData(e.currentTarget);
      await signUp(formData);
    } catch (err) {
      setError(err instanceof Error ? err.message : "An error occurred during sign up");
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <form className={`${styles.form} ${styles.signUp}`} onSubmit={handleSubmit}>
      {error && (
        <div className={styles.errorMessage}>
          {error}
        </div>
      )}

      <div className={styles.formRow}>
        <div className={styles.formGroup}>
          <label htmlFor="firstName" className={styles.label}>
            First Name *
          </label>
          <input
            type="text"
            id="firstName"
            name="firstName"
            placeholder="Enter your first name"
            className={styles.input}
            required
          />
        </div>

        <div className={styles.formGroup}>
          <label htmlFor="lastName" className={styles.label}>
            Last Name *
          </label>
          <input
            type="text"
            id="lastName"
            name="lastName"
            placeholder="Enter your last name"
            className={styles.input}
            required
          />
        </div>
      </div>

      <div className={styles.formGroup}>
        <label htmlFor="email" className={styles.label}>
          Email *
        </label>
        <input
          type="email"
          id="email"
          name="email"
          placeholder="Enter your email"
          className={styles.input}
          required
        />
      </div>

      <div className={styles.formRow}>
        <div className={styles.formGroup}>
          <label htmlFor="password" className={styles.label}>
            Password *
          </label>
          <input
            type="password"
            id="password"
            name="password"
            placeholder="Enter your password"
            className={styles.input}
            required
            minLength={6}
          />
        </div>

        <div className={styles.formGroup}>
          <label htmlFor="confirmPassword" className={styles.label}>
            Confirm Password *
          </label>
          <input
            type="password"
            id="confirmPassword"
            name="confirmPassword"
            placeholder="Confirm your password"
            className={styles.input}
            required
            minLength={6}
          />
        </div>
      </div>

      <div className={styles.formRow}>
        <div className={styles.formGroup}>
          <label htmlFor="favTeam" className={styles.label}>
            Favorite Team
          </label>
          <input
            type="text"
            id="favTeam"
            name="favTeam"
            placeholder="e.g., Mercedes, Ferrari, Red Bull"
            className={styles.input}
          />
        </div>

        <div className={styles.formGroup}>
          <label htmlFor="favDriver" className={styles.label}>
            Favorite Driver
          </label>
          <input
            type="text"
            id="favDriver"
            name="favDriver"
            placeholder="e.g., Lewis Hamilton, Max Verstappen"
            className={styles.input}
          />
        </div>
      </div>

      <button 
        type="submit" 
        className={styles.submitButton}
        disabled={isLoading}
      >
        {isLoading ? "Creating Account..." : "Create Account"}
      </button>

      <div className={styles.navLink}>
        Already have an account?{" "}
        <Link href="/sign-in" className={styles.link}>
          Sign In
        </Link>
      </div>
    </form>
  );
};

export default SignUpForm;
