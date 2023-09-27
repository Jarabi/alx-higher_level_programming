#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];
const characterId = 18;

request.get(apiUrl, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(body);
    const episodes = data.results;

    const characterList = episodes.map((episode) => {
      return episode.characters;
    });

    const antillesList = [];

    characterList.forEach((list) => {
      list.forEach(url => {
        if (url.includes(characterId)) {
          antillesList.push(url);
        }
      });
    });

    console.log(antillesList.length);
  }
});
