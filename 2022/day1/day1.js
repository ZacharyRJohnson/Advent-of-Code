"use strict";
exports.__esModule = true;
var fs_1 = require("fs");
var path_1 = require("path");
var part1 = function (input) {
    return (0, fs_1.readFileSync)((0, path_1.join)(__dirname, input), 'utf-8')
        .split('\r\n\r\n')
        .map(function (val) {
        return val.split('\n')
            .map(function (elfCals) {
            return Number(elfCals);
        }).reduce(function (agg, cal) { return agg + cal; }, 0);
    });
};
var ans = part1('in1.txt').sort(function (a, b) { return b - a; });
console.log(ans[0]);
console.log(ans.splice(0, 3).reduce(function (agg, val) { return agg + val; }, 0));
