#!/usr/bin/node

const fs = require('fs');
const file = process.argv[2] || '';
const encryption = 'utf8';

fs.readFile(
  file,
  encryption,
  function handleError (err, content) {
    if (err) {
      console.log(err);
    } else {
      console.log(content);
    }
  }
);
