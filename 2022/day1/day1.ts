import { readFileSync } from 'fs';
import {join} from 'path';

const part1 = (input) => {
    return readFileSync(join(__dirname, input), 'utf-8')
        .split('\r\n\r\n')
        .map((val) => 
            val.split('\n')
            .map((elfCals) => 
                Number(elfCals)).reduce((agg, cal) => agg+cal, 0));
}

const ans = part1('in1.txt').sort((a,b)=>b-a)
console.log(ans[0])
console.log(ans.splice(0, 3).reduce((agg, val) => agg+val,))