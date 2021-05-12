'use strict';

$(document).ready(() => {
  const itemList = $('.my_list');
  const addItemElem = $('#add_item');
  const removeItemElem = $('#remove_item');
  const clearListElem = $('#clear_list');

  addItemElem.click(() => itemList.append('<li>Item</li>'));
  removeItemElem.click(() => itemList.children().first().remove());
  clearListElem.click(() => itemList.children().remove());
});
