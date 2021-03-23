#!/usr/bin/node
'use strict';

const Rectangle = require('./5-square');

class Square extends Rectangle {
  charPrint (c) {
    super.print(c);
  }
}

module.exports = Square;
