#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const url = process.argv[2] || '';
const filePath = process.argv[3] || '';
const encryption = 'utf8';

request(url, function handleResponse (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(filePath, body,
      {
        encoding: encryption,
        flag: 'w'
      },
      function handleError (err) {
        if (err) {
          console.log(err.message);
        }
      }
    );
  }
});
