"use client";

import React from "react";
import styles from "../shared/form.module.css";
import Link from "next/link";

const SignInForm = () => {
  return (
    <form className={styles.form}>
      <div className={styles.formGroup}>
        <label htmlFor="email" className={styles.label}>
          Email
        </label>
        <input
          type="email"
          id="email"
          placeholder="Enter your email"
          className={styles.input}
          required
        />
      </div>

      <div className={styles.formGroup}>
        <label htmlFor="password" className={styles.label}>
          Password
        </label>
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
          <input
            type="checkbox"
            className={styles.checkbox}
          />
          <span className={styles.checkboxText}>Remember me</span>
        </label>
        <Link href="/forgot-password" className={styles.forgotLink}>
          Forgot password?
        </Link>
      </div>

      <button type="submit" className={styles.submitButton}>
        Sign In
      </button>

      <div className={styles.navLink}>
        Don't have an account?{" "}
        <Link href="/signup" className={styles.link}>
          Sign Up
        </Link>
      </div>
    </form>
  );
};

export default SignInForm;
