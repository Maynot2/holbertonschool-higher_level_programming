#!/usr/bin/node
'use strcit';

const nums = process.argv.slice(2, process.argv.length).map(el => Number(el));
let max = nums[0];
let secondMax = nums[0];

for (let i = 0; i < nums.length; i++) {
  if (nums[i] >= max) max = nums[i];
  for (let j = 0; j < nums.length; j++) {
    if (nums[j] >= secondMax && nums[j] < max) {
      secondMax = nums[j];
    }
  }
}

console.log(secondMax);
