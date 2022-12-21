import { readFileSync } from 'fs';
import {join} from 'path';

const input = readFileSync(join(__dirname, 'in1.txt'), 'utf-8').split('\n');

type FakeDir = {
    size: number
    id: number
    parentId: number
    children: Map<string, FakeDir | FakeFile>
    name: string
};

const makeDir = (id: number, parentId: number, name: string): FakeDir => {
    return {
        size: 0,
        id,
        parentId,
        children: new Map(),
        name
    };
}

type FakeFile = {
    size: number
    name: string
    parentId: number
    children: any
};

// const buildTree = (commands) => {
//     const root: FakeDir = makeDir(0, -1, '/');
//     let ptr = root;
//     let parentMap = [];
//     let id = 0;
//     commands.forEach(command => {
//         console.log(command);
//         command = command.trim().split(' ');
//         switch (command[0]) {
//             case '$': 
//                 if (command[1] === 'cd') {
//                     if (command[2] === '..') {
//                         ptr = parentMap[ptr.parentId];
//                     }
//                     else {
//                         console.log('Going in: ' + ptr.children.get(command[2]));
//                         ptr = ptr.children.get(command[2]) instanceof makeDir ? ptr.children.get(command[2]): undefined;
//                         //dirSize += exec(commands);
//                     }
//                 }
//                 break;
//             case 'dir':
                
//                 ptr.children.set(command[1], makeDir(ptr, command[1]));
//                 break;
//             default:
//                 ptr.size += Number(command[0]);
//                 ptr.children
//                     .set(command[1],
//                         {
//                             size: Number(command[0]), 
//                             name: command[1], 
//                             parent: ptr,
//                             children: undefined
//                         });
                
//         }
//         console.log(ptr)
//     });
//     return root;
// }

// const exec = (commands) => {
//     let command = commands.pop().trim().split(' ');
//     let dirSize = 0;
//     let moveOut = false;
//     while (!moveOut) {
//         switch (command[0]) {
//             case undefined:
//                 break;
//             case '$': 
//                 if (command[1] === 'cd') {
//                     if (command[2] === '..') {
//                         moveOut = true;
//                     }
//                     else {
//                         dirSize += exec(commands);
//                     }
//                 }
//                 break;
//             case 'dir':
//         }
//     }

//     return dirSize <= 100000 ? dirSize : 0;
// };

const part1 = (commands) => {
    let dirStack: Array<number> = [];
    let dirSize = 0;
    let ans = 0;
    commands.forEach(command => {
        command = command.trim().split(' ');
        switch (command[0]) {
            case '$': 
                if (command[1] === 'cd') {
                    if (command[2] === '..') {
                        if (dirSize < 100000) {
                            ans += dirSize;
                        }
                        dirSize = dirSize + dirStack.pop();
                    }
                    else {
                        dirStack.push(dirSize)
                        dirSize = 0;
                    }
                }
                break;
            case 'dir':
                break;
            default:
                dirSize += Number(command[0]);
        }
    });
    return ans;
};

const part2 = (commands) => {
    let dirStack: Array<number> = [];
    let dirSize = 0;
    let dirs: Map<string, number>;
    commands.forEach(command => {
        command = command.trim().split(' ');
        switch (command[0]) {
            case '$': 
                if (command[1] === 'cd') {
                    if (command[2] === '..') {
                        dirSizes.push(dirSize);
                        dirSize = dirSize + dirStack.pop();
                    }
                    else {
                        dirStack.push(dirSize);
                        dirSize = 0;
                    }
                }
                break;
            case 'dir':
                break;
            default:
                dirSize += Number(command[0]);
        }
    });
    dirSizes.push(dirSize);
    dirSizes.push(dirSize + dirStack.pop());
    dirSizes.sort((a, b) => a - b);
    let unused = 70000000 - dirSizes[dirSizes.length - 1];
    console.log(unused);
    for (let i = 0; i < dirSizes.length; i++) {
        if (unused + dirSizes[i] > 30000000) {
            return dirSizes[i];
        }
    }
    return -1;
};
console.log(part1(input));
console.log(part2(input));