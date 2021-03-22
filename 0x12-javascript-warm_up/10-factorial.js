#!/usr/bin/node
'use strcit';

const x = Number(process.argv[2]);

function factorial (num) {
  if (isNaN(num) || x < 2) return 1;

  return num * factorial(num - 1);
}

console.log(factorial(x));
