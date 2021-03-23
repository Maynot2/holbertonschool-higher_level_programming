#!/usr/bin/node
'use strict';

const Rectangle = require('./5-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    super.print(c);
  }
}

module.exports = Square;
