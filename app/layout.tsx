import type { Metadata } from "next";
import "./globals.css";
import AuthProvider from "@/components/providers/session-provider";
import { auth } from "@/auth";

export const metadata: Metadata = {
  title: "Race Predictor",
  description: "F1 Race Prediction Platform",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body>
        <AuthProvider>
          {children}
        </AuthProvider>
      </body>
    </html>
  );
}
