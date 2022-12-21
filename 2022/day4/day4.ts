import { readFileSync } from 'fs';
import {join} from 'path';

const part1 = (input) => {
    let overlap = readFileSync(join(__dirname, input), 'utf-8')
        .split('\n')
        .map((pair) => {
            return pair.split(',')
                .map((range) => {
                    return range.split('-')
                         .map((num) => Number(num));
                });
        });
    let tot = 0;
    overlap.forEach(pair => {
        let doesOverlap = 0
        if (pair[0][0] <= pair[1][0]) {
            if (pair[0][1] >= pair[1][1]) {
                doesOverlap = 1;
            }
        }
        if (pair[0][0] >= pair[1][0]) {
            if (pair[0][1] <= pair[1][1]){
                
                doesOverlap = 1;
            }
        }
        tot += doesOverlap;
    });
    return tot;
};

const part2 = (input) => {
    let overlap = readFileSync(join(__dirname, input), 'utf-8')
        .split('\n')
        .map((pair) => {
            return pair.split(',')
                .map((range) => {
                    return range.split('-')
                         .map((num) => Number(num));
                });
        });
    let tot = 0;
    overlap.forEach(pair => {
        let doesntOverlap = 0
        if (pair[0][0] > pair[1][1]) {
            console.log(pair);
            doesntOverlap = 1;
        }
        if (pair[0][1] < pair[1][0]) {
            console.log(pair);
            doesntOverlap = 1;
        }

        // if (pair[0][0] < pair[1][0]) {
        //     if (pair[0][1] < pair[1][0]) {
        //         doesntOverlap = 1;
        //     }
        // }
        // if (pair[0][0] > pair[1][0]) {
        //     if (pair[0][1] > pair[1][0]){
                
        //         doesntOverlap = 1;
        //     }
        // }
        // if (pair[1][0] < pair[0][0]) {
        //     if (pair[1][1] < pair[0][0]) {
        //         doesntOverlap = 1;
        //     }
        // }
        // if (pair[1][0] > pair[0][1]) {
        //     if (pair[1][1] > pair[0][1]){
                
        //         doesntOverlap = 1;
        //     }
        // }
        tot += doesntOverlap;
    });
    return overlap.length - tot;
};

console.log(part1('in1.txt'));
console.log(part2('in1.txt'));