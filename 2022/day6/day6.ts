import { readFileSync } from 'fs';
import {join} from 'path';

const isUnique = (chunk: string) => {
    for (let i = 0; i < chunk.length - 1; i++) {
        for (let j = i+1; j < chunk.length; j++) {
            if (chunk[i] === chunk[j]) 
                return false;
        }
    }
    return true;
};

const part1 = (input: string) => {
    const signal = readFileSync(join(__dirname, input), 'utf-8').trim();
    for (let i = 0; i < signal.length - 4; i++) {
        let chunk = signal.slice(i, i+4);
        if (isUnique(chunk))
            return i+4;
    }
    return undefined;
};

const part2 = (input: string) => {
    const signal = readFileSync(join(__dirname, input), 'utf-8').trim();
    for (let i = 0; i < signal.length - 14; i++) {
        let chunk = signal.slice(i, i+14);
        if (isUnique(chunk))
            return i+14;
    }
    return undefined;
};


console.log(part1('in1.txt'));
console.log(part2('in1.txt'));