#!/usr/bin/node

const fs = require('fs');
const file = process.argv[2];
const encryption = 'utf8';

try {
  const fileContent = fs.readFileSync(file, encryption);
  console.log(fileContent);
} catch (err) {
  console.log(err);
}
