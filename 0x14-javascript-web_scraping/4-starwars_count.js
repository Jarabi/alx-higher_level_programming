#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];
// const apiUrl = `${baseUrl}18`;

request.get(apiUrl, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(body);
    const episodes = data.results;
    const characterUrl = 'https://swapi-api.alx-tools.com/api/people/18/';
    let count = 0;

    episodes.forEach((episode) => {
      if (episode.characters.includes(characterUrl)) {
        count += 1;
      }
    });

    console.log(count);
  }
});
