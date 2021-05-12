'use strict';

const $ = window.$;
const header = $('header');
const updateHeader = $('#update_header');

updateHeader.click(() => {
  header.text('New Header!!!');
});
