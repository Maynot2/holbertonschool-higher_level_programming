'use strict';

$(document).ready(() => {
  const translateBtn = $('#btn_translate');
  const helloTranslationElem = $('#hello');

  translateBtn.click(() => {
    const inputLang = $('#language_code').val();
    const url = `https://fourtonfish.com/hellosalut/?lang=${inputLang}`;

    $.getJSON(url, (langObj) => {
      helloTranslationElem.text(langObj.hello);
    });
  });
});
