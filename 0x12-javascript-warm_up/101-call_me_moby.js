#!/usr/bin/node
'use strcit';

function callMeMoby (x, fn) {
  for (let i = 0; i < x; i++) {
    fn();
  }
}

exports.callMeMoby = callMeMoby;
