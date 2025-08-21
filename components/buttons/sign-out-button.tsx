'use client'

import { logout } from "@/lib/actions/auth"
import styles from "./buttons.module.css"

export const SignOutButton = () => {
   return (
     <button 
       onClick={() => logout()} 
       className={`${styles.button} ${styles.danger} ${styles.ripple}`}
     >
       Sign Out
     </button>
   )
}