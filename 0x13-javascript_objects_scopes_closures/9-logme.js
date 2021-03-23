#!/usr/bin/node
'use strict';

let counter = 0;

function logMe (item) {
  console.log(`${counter}: ${item}`);
  counter++;
}

exports.logMe = logMe;
