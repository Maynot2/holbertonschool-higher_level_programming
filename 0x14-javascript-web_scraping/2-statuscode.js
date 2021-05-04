#!/usr/bin/node

const request = require('request');
const url = process.argv[2] || '';

request(url, function handleResponse (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    console.log(`Code: ${res.statusCode}`);
  }
});
