#!/usr/bin/node

const fs = require('fs');
const filePath = process.argv[2] || '';
const content = process.argv[3]
const encryption = 'utf8';

fs.writeFile(filePath, content, 
  { encoding: encryption,
    flag: 'w'},
  function handleError(err) {
    if (err) {
      console.log(err.message)
    }
  }
);
