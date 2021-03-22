#!/usr/bin/node
'use strcit';

const nums = process.argv.slice(2, process.argv.length).reduce((acc, curr) => {
  if (Number(curr)) acc.push(Number(curr));
  return acc;
}, []);

if (nums.length < 2) {
  console.log(0);
} else {
  console.log(nums.sort((a, b) => b - a)[1]);
}
