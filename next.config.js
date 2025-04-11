// next.config.js
module.exports = {
  // Next.js automatically adds the webpack 5 support. 
  // You can still opt in to use webpack 5 by adding the "future" field to your next.config.js
  future: {
    webpack5: true,
  },

  // Configure Next.js' performance hints. This option gives you warnings if your bundles are too big. 
  // Default is "warning", but you can use "error" to make it more strict.
  performance: {
    hints: process.env.NODE_ENV === 'production' ? 'warning' : false,
  },

  // The Webpack's "publicPath" option is set by Next.js. 
  // You cannot modify the "output.publicPath" value.
  webpack: (config, { buildId, dev, isServer, defaultLoaders, webpack }) => {
    //