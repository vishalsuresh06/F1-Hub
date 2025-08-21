import React from 'react'
import { auth } from "@/auth";
import { SignOutButton } from '@/components/sign-out-button';

const UserInfo = async () => {
  const session = await auth();
    if (session?.user)
      return (
      <div>
        <h1>User signed in with name: {session.user.name}</h1>
        <h1>User signed in with email: {session.user.email}</h1>
        <SignOutButton/>
      </div>)
}

export default UserInfo
