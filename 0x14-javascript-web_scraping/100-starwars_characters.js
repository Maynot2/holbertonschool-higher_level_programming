#!/usr/bin/node

const request = require('request');
const url = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`;

request(url, function handleResponse1 (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    const movie = JSON.parse(body);
    for (const character of movie.characters) {
      request(character, function handleResponse2 (err, res, body) {
        if (err) {
          console.log(err);
        } else {
          const name = JSON.parse(body).name;
          console.log(name);
        }
      });
    }
  }
});
