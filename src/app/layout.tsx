tsx
// Importing necessary libraries and components
import React, { FC } from 'react';
import Head from 'next/head';

// Layout component
const Layout: FC = ({ children }) => {
    return (
        <>
            <Head>
                <title>My App</title>
                <meta name="viewport" content="initial-scale=1.0, width=device-width" />
                <meta charSet="utf-8" />
                <link rel="icon" href="/favicon.ico" />
                <meta name="description" content="Description of the app" />
            </Head>
            <main>{children}</main>
        </>
    );
};

export default Layout;

This is a layout file for a Next.js project written in TypeScript. The file includes a functional component Layout that wraps the children components. The Head component is used to modify the head of the page. The children are rendered inside the main tag. The FC (FunctionComponent) type is used to type the Layout component. This layout can be used to wrap pages or other components in your Next.js project.