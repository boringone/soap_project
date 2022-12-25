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
                test: /\.js(x?)$/,
                exclude: /node_modules/,
                use: [
                    'babel-loader'
                ],
                resolve: {
                    extensions: ['.js', '.jsx']
                }
            },
            {
                test: /\.css$/,
                use: [
                    'style-loader',
                    'css-loader'
                ],
            }
        ],
    }
}
