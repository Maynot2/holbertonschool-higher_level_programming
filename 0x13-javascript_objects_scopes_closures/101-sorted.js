#!/usr/bin/node
'use strict';

const occurencesById = require('./101-data').dict;

const idByOccurences = {};

for (const [id, occurence] of Object.entries(occurencesById)) {
  if (idByOccurences[occurence]) {
    idByOccurences[occurence].push(id);
  } else {
    idByOccurences[occurence] = [id];
  }
}

console.log(idByOccurences);
