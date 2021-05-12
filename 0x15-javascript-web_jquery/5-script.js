'use strict';

const $ = window.$;
const itemList = $('.my_list');
const addItem = $('#add_item');

addItem.click(() => {
  itemList.append('<li>Item</li>');
});
