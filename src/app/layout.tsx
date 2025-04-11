tsx
// Import necessary dependencies
import React, { ReactNode } from 'react'
import Head from 'next/head'
import Image from 'next/image'
import Link from 'next/link'

// Define types for children prop
interface IProps {
  children: ReactNode;
}

// Export default function component
export default function Layout({ children }: IProps): JSX.Element {
  return (
    <div>
      {/* Set up metadata */}
      <Head>
        <title>My Next.js App</title>
        <meta name="viewport" content="initial-scale=1.0, width=device-width" />
      </Head>

      {/* Set up header */}
      <header>
        <Link href="/">
          <a>
            <Image
              src="/logo.png"
              alt="Logo"
              width={150}
              height={50}
            />
          </a>
        </Link>
      </header>

      {/* Render children */}
      {children}

      {/* Set up footer */}
      <footer>
        <p>&copy; {new Date().getFullYear()} My Next.js App - All rights reserved</p>
      </footer>
    </div>
  )
}


This is a root layout file which includes the common layout for all pages, like the header and footer. It's written in TypeScript and follows Next.js best practices. The `Layout` component takes `children` as a prop, which will be the content of individual pages, and wraps them in a common layout. The layout includes a `Head` component for metadata, a `header` with a linked logo, and a `footer`.