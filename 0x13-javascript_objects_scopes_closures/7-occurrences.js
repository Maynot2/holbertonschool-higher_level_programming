#!/usr/bin/node
'use strict';

function nbOccurences (list, el) {
  return list.filter(elem => elem === el).length;
}

exports.nbOccurences = nbOccurences;
