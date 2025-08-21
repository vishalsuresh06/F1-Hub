import NextAuth from "next-auth";
import GitHub from 'next-auth/providers/github'

export const {auth, handlers, signIn, signOut} = NextAuth({
    providers: [GitHub],
    session: {
        strategy: "jwt",
    },
    callbacks: {
        async session({ session, token }) {
            if (token.sub && session.user) {
                session.user.id = token.sub;
            }
            return session;
        },
        async jwt({ token, user }) {
            if (user) {
                token.sub = user.id;
            }
            return token;
        },
    },
})