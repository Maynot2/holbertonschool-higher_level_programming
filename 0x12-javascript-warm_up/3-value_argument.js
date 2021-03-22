#!/usr/bin/node
'use strict';

const firstArg = process.argv[2];

if (firstArg) {
  console.log(firstArg);
} else {
  console.log('No argument');
}
