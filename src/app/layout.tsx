tsx
// Import necessary libraries
import React, { FC } from "react";
import Head from "next/head";
import { createGlobalStyle, ThemeProvider } from 'styled-components';

// Create global styles using styled-components
const GlobalStyle = createGlobalStyle`
  body {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
  }
`;

// Define your theme object (can be anything you want it to be)
const theme = {
  colors: {
    primary: '#0070f3',
  },
};

// Create a wrapper component for layout
const Layout: FC = ({ children }) => (
  <ThemeProvider theme={theme}>
    <GlobalStyle />
    <Head>
      <title>Your App Title</title>
      <meta name="viewport" content="initial-scale=1.0, width=device-width" />
      <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap" />
    </Head>
    <main>{children}</main>
  </ThemeProvider>
);

export default Layout;


This `Layout` component includes global layout configurations and CSS styling. We're using `styled-components` to create a global style and theme. We're using Next.js's `Head` component to add common metadata.

This is a TypeScript file, and we're using the `FC` (Function Component) type for our `Layout` component. This component takes `children` as a prop, which is the standard way to allow other components to be passed into this component.

Please replace `'Your App Title'` with your app's title and make any necessary adjustments to the theme object and global styles to suit your needs.