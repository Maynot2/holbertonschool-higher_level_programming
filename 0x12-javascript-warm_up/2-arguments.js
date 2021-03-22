#!/usr/bin/node
'use strict';

const argsCount = process.argv.length;

if (argsCount < 3) {
  console.log('No argument');
} else if (argsCount === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
