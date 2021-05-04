#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const characterId = '18';

request(url, function handleResponse (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    let counter = 0;
    const films = JSON.parse(body).results;
    for (const film of films) {
      for (const character of film.characters) {
        if (character.includes(characterId)) {
          counter++;
        }
      }
    }
    console.log(counter);
  }
});
