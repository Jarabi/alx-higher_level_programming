#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];

if (!movieId) {
  console.log('Enter movie ID');
  process.exit(1);
}

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

const fetchMovies = (url, id) => {
  request.get(apiUrl, (err, res, body) => {
    if (err) {
      console.log(err);
    } else {
      const movies = JSON.parse(body);
      fetchCharacters(movies);
    }
  });
};

const fetchCharacters = (movies) => {
  movies.characters.forEach((characterUrl) => {
    request.get(characterUrl, (err, res, body) => {
      if (err) {
        console.log(err);
      } else {
        const character = JSON.parse(body);
        console.log(character.name);
      }
    });
  });
};

fetchMovies(apiUrl, movieId);
