function getVector(w) {
    let idx = wordIndex[w];
    if (idx === undefined) throw new Error('Word not found: ' + w);
    return vectors.subarray(idx * dims, (idx + 1) * dims);
}
function modulus(a) {
    return Math.sqrt(a.map(v => v * v).reduce((a, v) => a + v));
}
function normalize(a) {
    const mul = 1 / modulus(a);
    return a.map(v => v * mul);
}
function dot(a, b) {
    return a.map((v, i) => v * b[i]).reduce((a, v) => a + v)
}
function similarity(a, b) {
    return dot(a, b) / modulus(a) / modulus(b);
}
function similarityNorm(a, b) {
    return dot(a, b) / modulus(b);
}
function subSum(a, b, c) {
    return a.map((v, i) => v - b[i] + c[i]);
}
class Similarity {
    word;
    similarity;
    constructor(word, similarity) {
    this.word = word;
    this.similarity = similarity;
    }
    toString() {
    return this.word + ' ' + this.similarity.toFixed(5);
    }
}
function allSimilarities(w0) {
    const v = normalize(typeof w0 == 'string' ? getVector(w0) : w0);
    const s = words.map(w => new Similarity(w, similarityNorm(v, getVector(w))));
    s.sort((a, b) => b.similarity - a.similarity);
    return s;
}

const resp = await fetch('fasttext-it-mini.wv.out');
// const resp = await fetch('cc.it.300.bin.nat.lower.txt.out');
const buf = await resp.arrayBuffer();
const utf8 = new TextDecoder();
let tmp = utf8.decode(new DataView(buf, 0, 100)).split('\n')[0].split(' ');
const wordsSize = +tmp[0];
const dims = +tmp[1];
console.log('Size ' + buf.byteLength);
console.log('Loading ' + wordsSize + '×' + dims);
const headerSize = buf.byteLength - wordsSize * dims * 4;
const vectors = new Float32Array(buf, headerSize);
tmp = utf8.decode(new DataView(buf, 0, headerSize)).split('\n').slice(1, wordsSize + 1);
const words = tmp;
console.log(words);
const wordIndex = {};
words.forEach((v, i) => wordIndex[v] = i);
console.log(vectors.slice(0, dims));
console.log(modulus(vectors.subarray(0, dims)));

// console.log(wordIndex['rosso']);
// console.log(wordIndex['verde']);
// console.log(similarity(getVector('rosso'), getVector('verde')));

const t0 = Date.now();
for (const w of ['ciao', 'simpatia', 'asciutto'])
    console.log(w, '~', allSimilarities(w).slice(1, 11).join(', '));
const t1 = Date.now();
console.log('Speed:', t1 - t0);

console.log('re - regina + cane', '~', allSimilarities(subSum(getVector('re'), getVector('regina'), getVector('cane'))).slice(0, 10).join(', '));
