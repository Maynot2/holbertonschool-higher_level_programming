'use strict';

const $ = window.$;
const header = $('header');
const trigger = $('#toggle_header');

trigger.click(() => {
  header.toggleClass('green');
  header.toggleClass('red');
});
