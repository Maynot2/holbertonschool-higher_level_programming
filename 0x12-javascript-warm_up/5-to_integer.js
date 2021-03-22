#!/usr/bin/node
'use strict';

const num = Number(process.argv[2]);

if (num) {
  console.log(`My number: ${Math.trunc(num)}`);
} else {
  console.log('Not a number');
}
