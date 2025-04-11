js
// next.config.js

// Include necessary Next.js configuration
const path = require('path');
const withCSS = require('@zeit/next-css');
const withImages = require('next-images');

module.exports = withImages(
  withCSS({
    // Set up proper build settings
    webpack(config, options) {
      config.resolve.alias['components'] = path.join(__dirname, 'components');
      return config;
    },

    // Configure output settings
    distDir: 'build',

    // Enable React Strict Mode
    reactStrictMode: true,

    // Runtime Configuration
    publicRuntimeConfig: {
      // Will be available on both server and client
      staticFolder: '/static',
    },

    // Next.js API Routes
    api: {
      bodyParser: {
        sizeLimit: '1mb',
      },
    },

    // Next.js Images
    images: {
      domains: ['example.com'],
    },

    // Next.js CSS
    cssModules: true,
  })
);

In this `next.config.js` file, we're:
- Configuring Next.js to handle CSS and image imports with the `@zeit/next-css` and `next-images` libraries
- Setting up a custom alias for the `components` directory
- Configuring the output directory to be `build` instead of `.next`
- Enabling React Strict Mode, which can help to find potential problems in an application during development
- Setting up a runtime configuration that will make the `/static` path available on both server and client
- Configuring Next.js API routes to limit the body parser size to 1mb
- Configuring Next.js to handle images from `example.com`
- Enabling CSS Modules, which is a CSS file in which all class names and animation names are scoped locally by default