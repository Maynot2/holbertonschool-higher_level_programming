'use strict';

const $ = window.$;
const movieListElem = $('#list_movies');
const url = 'https://swapi-api.hbtn.io/api/films/?format=json'

$.getJSON(url, (movieObj) => {
  const movies = movieObj.results
  for (const movie of movies) {
    movieListElem.append(`<li>${movie.title}</li>`);
  }
});
