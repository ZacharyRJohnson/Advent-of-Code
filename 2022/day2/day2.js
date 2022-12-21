"use strict";
exports.__esModule = true;
var fs_1 = require("fs");
var path_1 = require("path");
var part1 = function (input) {
    return (0, fs_1.readFileSync)((0, path_1.join)(__dirname, input), 'utf-8')
        .split('\n').map(function (turn) {
        var splitT = turn.trim().split(' ');
        var opp = -1;
        var you = -1;
        // console.log(splitT)
        switch (splitT[0]) {
            case ('A'):
                opp = 1;
                break;
            case ('B'):
                opp = 2;
                break;
            case ('C'):
                opp = 3;
        }
        switch (splitT[1]) {
            case ('X'):
                you = 1;
                break;
            case ('Y'):
                you = 2;
                break;
            case ('Z'):
                you = 3;
        }
        var diff = you - opp;
        var tot = 0;
        // console.log(diff)
        // console.log(you)
        if (you === opp)
            tot = you + 3;
        else if ((opp) % 3 + 1 === you)
            tot = you + 6;
        else
            tot = you + 0;
        return tot;
    });
};
var part2 = function (input) {
    return (0, fs_1.readFileSync)((0, path_1.join)(__dirname, input), 'utf-8')
        .split('\n').map(function (turn) {
        var splitT = turn.trim().split(' ');
        var opp = -1;
        var you = -1;
        // console.log(splitT)
        switch (splitT[0]) {
            case ('A'):
                opp = 1;
                break;
            case ('B'):
                opp = 2;
                break;
            case ('C'):
                opp = 3;
        }
        switch (splitT[1]) {
            case ('X'):
                you = (opp - 1) == 0 ? 3 : opp - 1;
                //console.log(you + 0)
                return you + 0;
            case ('Y'):
                you = opp;
                //console.log(you + 3)
                return you + 3;
            case ('Z'):
                you = (opp) % 3 + 1;
                //console.log(you + 6)
                return you + 6;
        }
    });
};
console.log(part1('in1.txt').reduce(function (agg, val) { return agg + val; }, 0));
console.log(part2('in1.txt').reduce(function (agg, val) { return agg + val; }, 0));
