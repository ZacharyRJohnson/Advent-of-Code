import { readFileSync } from 'fs';
import {join} from 'path';

const getPriority = (item: string) => {
    const lowerOffset = 96;
    const upperOffset = 38;
    if (item === item.toUpperCase())
        return item.charCodeAt(0) - upperOffset;
    else
        return item.charCodeAt(0) - lowerOffset;
}

const part1 = (input) => {

    const rucksacks = readFileSync(join(__dirname, input), 'utf-8').split("\n");
    let total = 0;
    rucksacks.forEach(sack => {
        sack = sack.trim();
        let seen: {[id: string] : Number} = {};
        for (let i = 0; i < sack.length/2; i++) {
            for (let j = sack.length/2; j < sack.length; j++) {
                if (sack[j] === sack[i]) {
                    total += !seen[sack[j]] ? getPriority(sack[j]) : 0;
                    seen[sack[j]] = 1;
                }
            }
        }
    });
    return total;
};

const getBadgeValue = (group: string[]) => {
    for (let i1 = 0; i1 < group[0].length; i1++){
        const item1 = group[0][i1];
        for (let i2 = 0; i2 < group[1].length; i2++) {
            const item2 = group[1][i2];
            if (item1 === item2) {
                for (let i3 = 0; i3 < group[2].length; i3++) {
                    const item3 = group[2][i3];
                    if (item2 === item3) {
                        return getPriority(item3);
                    }
                }
            }                
        }
    }
};

const part2 = (input) => {
    const rucksacks = readFileSync(join(__dirname, input), 'utf-8').split("\n");
    let total = 0;
    for (let i = 0; i < rucksacks.length; i+= 3) {
        const group = rucksacks.slice(i, i + 3);
        total += getBadgeValue(group);
    }
    return total;
};

console.log(part1('in1.txt'));
console.log(part2('in1.txt'));