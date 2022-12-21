import { readFileSync } from 'fs';
import {join} from 'path';

const part1 = (input) => {
    const [crates, instructions] = readFileSync(join(__dirname, input), 'utf-8').split('\r\n\r\n');

    let t = crates.split('\n');
    let numStacks = t.pop().replace(/\s+/g, '').length;
    let locsGrid: string[][] = [];
    for (let i = 0; i < numStacks; i++) {
        locsGrid.push([]);
    }
    t.forEach(row => {
        let ind = 0;
        for (let i = 0; i < row.length; i += 4) {
            let chunk = row.slice(i, i+4);
            chunk = chunk.indexOf('[') === -1 ? '': chunk[chunk.indexOf('[') + 1];
            if (chunk !== '')
                locsGrid[ind].push(chunk);
            ind++;
        }
    });
    
    locsGrid.map(row => row.reverse());
    let insts: number[][] = [];
    instructions.split('\n').forEach(row => {
        const line = row.split(' ');
        insts.push([Number(line[1]), Number(line[3]), Number(line[5])])
    });

    insts.forEach(([numCrates, start, end]) => {
        for (let i = 0; i < numCrates; i++) {
            locsGrid[end-1].push(locsGrid[start-1].pop());
        }
    });

    return locsGrid.reduce((ans, stack) => ans+=stack.pop(), '');

};

const part2 = (input) => {
    const [crates, instructions] = readFileSync(join(__dirname, input), 'utf-8').split('\r\n\r\n');

    let t = crates.split('\n');
    let numStacks = t.pop().replace(/\s+/g, '').length;
    let locsGrid: string[][] = [];
    for (let i = 0; i < numStacks; i++) {
        locsGrid.push([]);
    }
    t.forEach(row => {
        let ind = 0;
        for (let i = 0; i < row.length; i += 4) {
            let chunk = row.slice(i, i+4);
            chunk = chunk.indexOf('[') === -1 ? '': chunk[chunk.indexOf('[') + 1];
            if (chunk !== '')
                locsGrid[ind].push(chunk);
            ind++;
        }
    });
    
    locsGrid.map(row => row.reverse());
    let insts: number[][] = [];
    instructions.split('\n').forEach(row => {
        const line = row.split(' ');
        insts.push([Number(line[1]), Number(line[3]), Number(line[5])])
    });

    insts.forEach(([numCrates, start, end]) => {
        let crane:string[] = []
        for (let i = 0; i < numCrates; i++) {
            crane.push(locsGrid[start-1].pop())
        }
        for (let i = 0; i < numCrates; i++) {
            locsGrid[end-1].push(crane.pop());
        }
    });

    return locsGrid.reduce((ans, stack) => ans+=stack.pop(), '');

};

console.log(part1('in1.txt'));
console.log(part2('in1.txt'));