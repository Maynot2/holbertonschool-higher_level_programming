'use strict';

$(document).ready(() => {
  const helloTranslationElem = $('#hello');
  const url = 'https://fourtonfish.com/hellosalut/?lang=fr';

  $.getJSON(url, (langObj) => {
    helloTranslationElem.text(langObj.hello);
  });
});
