#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];

if (!movieId) {
  console.log('Enter movie ID');
  process.exit(1);
}

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

const fetchMovies = (url) => {
  return new Promise((resolve, reject) => {
    request.get(url, (err, res, body) => {
      if (err) {
        reject(err);
      } else {
        const movies = JSON.parse(body);
        resolve(movies);
      }
    });
  });
};

const fetchCharacters = (movies) => {
  return Promise.all(
    movies.characters.map(async (characterUrl) => {
      return new Promise((resolve, reject) => {
        request.get(characterUrl, (err, res, body) => {
          if (err) {
            reject(err);
          } else {
            const character = JSON.parse(body);
            resolve(character.name);
          }
        });
      });
    })
  );
};

const main = async () => {
  try {
    const movies = await fetchMovies(apiUrl);
    const characters = await fetchCharacters(movies);

    characters.forEach(actor => {
      console.log(actor);
    });
  } catch (err) {
    console.error(err);
  }
};

main();
