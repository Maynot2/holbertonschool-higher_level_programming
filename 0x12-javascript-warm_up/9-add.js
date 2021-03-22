#!/usr/bin/node
'use strcit';

const x = Number(process.argv[2]);
const y = Number(process.argv[3]);

function add (a, b) {
  return a + b;
}

console.log(add(x, y));
