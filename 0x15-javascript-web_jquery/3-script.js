'use strict';

const $ = window.$;
const header = $('header');
const trigger = $('#red_header');

trigger.click(() => header.addClass('red'));
