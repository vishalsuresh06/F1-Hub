import React from 'react'
import { auth } from "@/auth";
import { SignOutButton } from '@/components/buttons/sign-out-button';
import { redirect } from 'next/navigation';
import styles from './dashboard.module.css';

const Dashboard = async ({
  searchParams,
}: {
  searchParams: { message?: string };
}) => {
  const session = await auth();
  
  if (!session?.user) {
    redirect('/sign-in');
  }

  return (
    <div className={styles.container}>
      <div className={styles.card}>
        {searchParams.message && (
          <div className={styles.message}>
            {searchParams.message}
          </div>
        )}
        
        <h1 className={styles.title}>
          Dashboard
        </h1>
        
        <h2 className={styles.subtitle}>
          Welcome, {session.user.name}!
        </h2>
        
        <p className={styles.email}>
          Email: {session.user.email}
        </p>
        
        <div className={styles.grid}>
          <div className={styles.cardItem}>
            <h3 className={styles.cardTitle}>
              Race Predictions
            </h3>
            <p className={styles.cardDescription}>
              Make your predictions for upcoming races
            </p>
          </div>
          
          <div className={styles.cardItemSecondary}>
            <h3 className={styles.cardTitleSecondary}>
              Leaderboard
            </h3>
            <p className={styles.cardDescription}>
              View your ranking and points
            </p>
          </div>
        </div>
        
        <div className={styles.actions}>
          <SignOutButton/>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;
