#!/usr/bin/node
'use strict';

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint(c) {
    super.print(c);
  }
}

module.exports = Square;
