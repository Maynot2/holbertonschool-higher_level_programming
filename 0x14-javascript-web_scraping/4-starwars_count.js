#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/people/18';

request(url, function handleResponse (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    const character = JSON.parse(body);
    console.log(character.films.length);
  }
});
