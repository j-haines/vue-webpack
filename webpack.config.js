const path = require("path")
const webpack = require("webpack")

const VueLoaderPlugin = require("vue-loader/lib/plugin")

const static_dir = path.resolve(__dirname, "static")

const dist_dir = path.resolve(static_dir, "dist")
const src_dir = path.resolve(static_dir, "src")

module.exports = {
    entry: path.resolve(src_dir, "main.js"),
    output: {
        path: dist_dir,
        publicPath: "/dist/",
        filename: "build.js",
    },
    module: {
        rules: [
            {
                test: /\.css$/,
                use: [
                    "vue-style-loader",
                    "css-loader",
                ],
            },
            {
                test: /\.s[ac]ss$/,
                use: [
                    "vue-style-loader",
                    "css-loader",
                    "sass-loader",
                ],
            },
            {
                test: /\.vue$/,
                loader: "vue-loader",
                options: {
                    loaders: {}
                },
            },
            {
                test: /\.js$/,
                loader: "babel-loader",
                exclude: /node_modules/,
            },
            {
                test: /\.(png|jpg|gif|svg)$/,
                loader: "file-loader",
                options: {
                    name: "[name].[ext]?[hash]",
                },
            },
        ],
    },
    plugins: [
        new webpack.ProvidePlugin({
            noUiSlider: "nouislider",
        }),
        new VueLoaderPlugin(),
    ],
    resolve: {
        alias: {
            "vue$": "vue/dist/vue.esm.js",
        },
        extensions: ["*", ".js", ".vue", ".json"],
    },
    devServer: {
        historyApiFallback: true,
        noInfo: true,
        overlay: true,
    },
    performance: {
        hints: false,
    },
    devtool: "eval-source-map",
}

if (process.env.NODE_ENV === "production") {
    module.exports.devtool = "source-map"
    module.exports.mode = "production"
    module.exports.optimization = {minimize: true}
    module.exports.plugins = (module.exports.plugins || []).concat([
        new webpack.DefinePlugin({
            "process.env": {
                NODE_ENV: '"production"',
            },
        }),
        new webpack.LoaderOptionsPlugin({
            minimize: true,
        }),
    ])
} else {
    module.exports.devtool = "eval-source-map"
    module.exports.mode = "development"
}