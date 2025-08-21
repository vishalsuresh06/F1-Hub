import SignUpForm from "@/components/sign-up-form/sign-up-form";
import styles from "../shared/auth-page.module.css";

export default function SignUpPage() {
  return (
    <div className={styles.container}>
      <div className={`${styles.content} ${styles.signUp}`}>
        <div className={styles.header}>
          <h1 className={styles.title}>Create Account</h1>
          <p className={styles.subtitle}>
            Join the race prediction community and start making your predictions!
          </p>
        </div>
        
        <SignUpForm />
      </div>
    </div>
  );
}
