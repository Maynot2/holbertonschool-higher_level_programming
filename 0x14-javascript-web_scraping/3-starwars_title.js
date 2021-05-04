#!/usr/bin/node

const request = require('request');
const url = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`;

request(url, function handleResponse (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    const movie = JSON.parse(body);
    console.log(movie.title);
  }
});
