import { readFileSync } from 'fs';
import {join} from 'path';

const part1 = (input) => {
    return readFileSync(join(__dirname, input), 'utf-8')
        .split('\n').map((turn) => {
            const splitT = turn.trim().split(' ');
            let opp = -1;
            let you = -1;
            switch(splitT[0]) {
                case('A'):
                    opp = 1;
                    break;
                case('B'):
                    opp = 2;
                    break;
                case('C'):
                    opp = 3
            }
            switch(splitT[1]) {
                case('X'):
                    you = 1;
                    break;
                case('Y'):
                    you = 2;
                    break;
                case('Z'):
                    you = 3
            }
            let tot = 0
            if (you === opp)
                tot= you + 3;
            else if ((opp)%3+1 === you)
                tot= you + 6;
            else
                tot= you + 0;
            return tot;

        })
}

const part2 = (input) => {
    return readFileSync(join(__dirname, input), 'utf-8')
        .split('\n').map((turn) => {
            const splitT = turn.trim().split(' ');
            let opp = -1;
            let you = -1;
            switch(splitT[0]) {
                case('A'):
                    opp = 1;
                    break;
                case('B'):
                    opp = 2;
                    break;
                case('C'):
                    opp = 3
            }
            switch(splitT[1]) {
                case('X'):
                    you = (opp-1) == 0 ? 3: opp-1;
                    return you + 0;
                case('Y'):
                    you = opp;
                    return you + 3;
                case('Z'):
                    you = (opp)%3+1;
                    return you + 6
            }
        })
}

console.log(part1('in1.txt').reduce((agg, val) => agg + val, 0));
console.log(part2('in1.txt').reduce((agg, val) => agg + val, 0));