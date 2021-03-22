#!/usr/bin/node
'use strcit';

const x = Number(process.argv[2]);
let square = '';

if (x > 0) {
  for (let i = 0; i < x; i++) {
    for (let j = 0; j < x; j++) {
      square += 'X';
    }
    if (i !== x - 1) square += '\n';
  }
  console.log(square);
} else if (x < 1) {
  // pass
} else {
  console.log('Missing size');
}
