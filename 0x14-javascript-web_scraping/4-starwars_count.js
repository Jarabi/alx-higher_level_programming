#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];

request.get(apiUrl, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(body);
    const episodes = data.results;
    const characterId = 18;
    const characterUrl = 'https://swapi-api.alx-tools.com/api/people/';

    const wedgeAntillesEpisodes = episodes.filter((episode) => {
      return episode.characters.includes(`${characterUrl}${characterId}/`);
    });

    console.log(wedgeAntillesEpisodes.length);
  }
});
