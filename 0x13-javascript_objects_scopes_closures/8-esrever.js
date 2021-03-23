#!/usr/bin/node
'use strict';

function esrever (list) {
  const newList = [];

  for (let i = list.length - 1; i >= 0; i--) {
    newList.push(list[i]);
  }

  return newList;
}

exports.esrever = esrever;
