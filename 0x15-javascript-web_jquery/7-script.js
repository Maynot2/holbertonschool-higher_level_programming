'use strict';

const $ = window.$;
const characterElem = $('#character');
const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json'

$.getJSON(url, (characterObj) => characterElem.text(characterObj.name));

