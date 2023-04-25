#!/bin/env node

import * as fs from 'node:fs';
import * as readline from 'node:readline';

// const name = 'fasttext-it-mini.wv';
const name = 'cc.it.300.bin.nat.lower.txt';

let line = 0, dims, words, weights;

readline.createInterface({
    input: fs.createReadStream(name)
}).on('line', function (s) {
    // console.log('Line', line);
    const w = s.split(' ');
    if (dims === undefined) {
        dims = +w[1];
        words = new Array(+w[0]);
        weights = new Float32Array(words.length * dims);
    } else {
        words[line] = w.shift();
        // weights.set(w.map(f => Math.round(f * 32768)), line * dims);
        weights.set(w, line * dims);
        ++line;
    }
}).on('close', function () {
    console.log('Loaded ' + words.length + '×' + dims);
    const out = fs.createWriteStream(name + '.out');
    const head = Buffer.from(words.length + ' ' + dims + '\n' + words.join('\n') + '\n', 'utf8');
    out.write(head);
    const next4 = ((head.length - 1) | 3) + 1;
    out.write(Buffer.alloc(next4 - head.length, '=')); // fill to align to next 4 bytes
    out.write(Buffer.from(weights.buffer));
});
