"use client";

import React from "react";
import styles from "./sign-in-form.module.css";
import Link from "next/link";
import { useState } from "react";
import { validateAccount } from "@/utils/account-validation";

const SignInForm = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [rememberMe, setRememberMe] = useState(false);

  const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();

  };

  return (
    <form className={styles.signInForm}>
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
          value={email}
          onChange={(e) => setEmail(e.target.value)}
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
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
      </div>

      <div className={styles.formOptions}>
        <label className={styles.checkboxLabel}>
          <input
            type="checkbox"
            className={styles.checkbox}
            checked={rememberMe}
            onChange={(e) => setRememberMe(e.target.checked)}
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
    </form>
  );
};

export default SignInForm;
