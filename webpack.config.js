const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const ReactRefreshWebpackPlugin = require('@pmmmwh/react-refresh-webpack-plugin');

module.exports = {
  entry: './src/index.js', // Entry point for the app
  output: {
    path: path.resolve(__dirname, 'dist'),
    filename: 'bundle.js', // Output file for the bundled code
  },
  module: {
    rules: [
      {
        test: /\.js$/, // Target JavaScript files
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader', // Use Babel for transpiling
          options: {
            plugins: [
              'react-refresh/babel', // Enable Fast Refresh
            ],
          },
        },
      },
      {
        test: /\.css$/, // Target CSS files
        use: ['style-loader', 'css-loader'],
      },
    ],
  },
  resolve: {
    extensions: ['.js', '.jsx'], // Resolve .js and .jsx extensions
  },
  devServer: {
    static: {
      directory: path.join(__dirname, 'dist'), // ✅ Correct replacement for `contentBase`
    },
    hot: true, // Enable Hot Module Replacement
    port: 3000,
    open: true, // Open browser automatically
    historyApiFallback: true, // Allows React Router to work with refresh
  },
  plugins: [
    new HtmlWebpackPlugin({
      template: './public/index.html', // Template for the index.html
    }),
    new ReactRefreshWebpackPlugin(), // Enable Fast Refresh
  ],
};