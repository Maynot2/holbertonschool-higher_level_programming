#!/usr/bin/node

const request = require('request');
const url = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`;

function getCharacter (url) {
  return new Promise(function requestUrl (resolve, reject) {
    request(url, function handleResponse2 (err, res, body) {
      if (err) {
        reject(err);
      } else {
        resolve(body);
      }
    });
  });
}

request(url, async function handleResponse1 (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    const movie = JSON.parse(body);
    for (const characterUrl of movie.characters) {
      const bodyCharacter = await getCharacter(characterUrl);
      const character = JSON.parse(bodyCharacter);
      console.log(character.name);
    }
  }
});
