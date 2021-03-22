#!/usr/bin/node
'use strcit';

function addMeMaybe (x, fn) {
  fn(x + 1);
}

exports.addMeMaybe = addMeMaybe;
