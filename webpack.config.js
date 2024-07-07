const path = require('path');

module.exports = {
    entry: './src/dice.js',
    output: {
        filename: 'bundle.js',
        path: path.resolve(__dirname, 'dist')
    }
};
