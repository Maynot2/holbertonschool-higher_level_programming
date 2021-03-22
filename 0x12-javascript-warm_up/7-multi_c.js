#!/usr/bin/node
'use strcit';

const x = Number(process.argv[2]);

if (x === 0 || x) {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
