const path = require('path');

module.exports = {
    mode: 'development',
    entry: path.resolve(__dirname, './assets/index.jsx'),
    output: {
        filename: 'main.js',
        path: path.resolve(__dirname, './static'),
    },
    module: {
        rules: [
            {
                test: /\.(js|jsx)$/,
                exclude: /node_modules/,
                loader: 'babel-loader',
                options: {presets: ["@babel/preset-env", "@babel/preset-react"]}
            }
        ]
    }
}