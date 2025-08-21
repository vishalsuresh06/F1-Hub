import SignInForm from "@/components/sign-in-form/sign-in-form";
import styles from "../shared/auth-page.module.css";

export default function SignInPage() {
  return (
    <div className={styles.container}>
      <div className={`${styles.content} ${styles.signIn}`}>
        <div className={styles.header}>
          <h1 className={styles.title}>Welcome Back</h1>
          <p className={styles.subtitle}>
            Sign in to your account to continue making race predictions
          </p>
        </div>
        
        <SignInForm />
      </div>
    </div>
  );
}
