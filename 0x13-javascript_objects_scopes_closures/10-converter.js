#!/usr/bin/node
'use strict';

function converter (base) {
  return function (num) {
    return num.toString(base);
  }
}

exports.converter = converter;
