// Project sponsor is https://ec.europa.eu/isa2/
// License is https://joinup.ec.europa.eu/community/eupl/og_page/eupl

const ExtractTextPlugin = require("extract-text-webpack-plugin");
const webpack = require("webpack");

const config = module.exports = {
    context: __dirname,
    entry: "./index.js",
    output: {
        path: __dirname + "/../eli_annotation/static",
        filename: "bundle.js"
    },
    module: {
        rules: [
            {
                test: /\.css$/,
                use: ExtractTextPlugin.extract({
                    fallback: "style-loader",
                    use: "css-loader"
                })
            },
            {
                test: /\.js$/,
                exclude: /node_modules/,
                loader: 'babel-loader',
                options: {
                    presets: ['react', 'latest', 'flow']
                }
            }
        ]
    },
    plugins: [
        new ExtractTextPlugin("bundle.css")
    ],
    externals: {
        "jquery": "jQuery",
        "react": "React",
        "react-dom": "ReactDOM",
        'react/addons': true,
        'react/lib/ExecutionEnvironment': true,
        'react/lib/ReactContext': true
    }
};

if (process.env.NODE_ENV === 'production') {
    // use react.min
    config.plugins.push(
            new webpack.DefinePlugin({
            'process.env': {NODE_ENV: JSON.stringify('production')}
            }));
}
