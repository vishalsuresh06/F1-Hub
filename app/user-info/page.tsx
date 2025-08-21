import React from 'react'
import { auth } from "@/auth";
import { SignOutButton } from '@/components/buttons/sign-out-button';
import { redirect } from 'next/navigation';

const UserInfo = async ({
  searchParams,
}: {
  searchParams: { message?: string };
}) => {
  const session = await auth();
  
  if (!session?.user) {
    redirect('/sign-in');
  }

  return (
    <div style={{
      minHeight: '100vh',
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
      background: 'linear-gradient(135deg, #0f0f23 0%, #1a1a2e 50%, #16213e 100%)',
      padding: '2rem'
    }}>
      <div style={{
        background: 'rgba(21, 21, 30, 0.9)',
        backdropFilter: 'blur(10px)',
        borderRadius: '20px',
        padding: '3rem 2rem',
        boxShadow: '0 20px 40px rgba(0, 0, 0, 0.3)',
        border: '1px solid rgba(148, 148, 152, 0.1)',
        maxWidth: '500px',
        width: '100%',
        textAlign: 'center'
      }}>
        {searchParams.message && (
          <div style={{
            background: 'rgba(34, 197, 94, 0.1)',
            border: '1px solid rgba(34, 197, 94, 0.3)',
            color: '#4ade80',
            padding: '0.75rem 1rem',
            borderRadius: '8px',
            marginBottom: '2rem',
            fontSize: '0.875rem'
          }}>
            {searchParams.message}
          </div>
        )}
        
        <h1 style={{
          fontSize: '2rem',
          fontWeight: '800',
          color: '#ffffff',
          marginBottom: '1rem',
          textTransform: 'uppercase',
          letterSpacing: '2px'
        }}>
          Welcome, {session.user.name}!
        </h1>
        
        <p style={{
          color: '#949498',
          fontSize: '1rem',
          marginBottom: '2rem'
        }}>
          Email: {session.user.email}
        </p>
        
        <div style={{
          display: 'flex',
          flexDirection: 'column',
          gap: '1rem',
          alignItems: 'center'
        }}>
          <SignOutButton/>
        </div>
      </div>
    </div>
  );
};

export default UserInfo
