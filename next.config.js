// Importing necessary modules
const path = require('path');

module.exports = {
    // Setting up Next.js build settings
    distDir: 'build',

    // Customizing Webpack configuration
    webpack: (config, { buildId, dev, isServer, defaultLoaders, webpack }) => {
        config.resolve.alias['@'] = path.resolve(__dirname);
        return config;
    },

    // Output settings configuration
    images: {
        domains: ['localhost', 'example.com'], // Replace with your image domains
    },

    // Enable React strict mode
    reactStrictMode: true,

    // Next.js API Routes configuration
    api: {
        bodyParser: {
            sizeLimit: '1mb', // You can adjust the size limit as per your requirement
        },
    },

    // Environment variables to be exposed to the browser
    env: {
        customKey: process.env.customKey, // Replace 'customKey' with your actual key name
    },
};

This is an example code for `next.config.js` file. A few things to note here:

1. The `distDir` config changes the directory where the build output is placed.
2. Webpack can be customized by adding a `webpack` function.
3. `images` allows you to define which domains are allowed to host your images if you are using the `next/image` component.
4. `reactStrictMode` enables React's Strict Mode, a development mode feature which helps to highlight potential problems in an application.
5. `api` is used to configure API routes.
6. `env` allows you to specify environment variables that should be available on the client side.

Remember to replace placeholders with actual values according to your project needs.