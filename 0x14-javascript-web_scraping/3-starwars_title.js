#!/usr/bin/node
const request = require('request');

const id = process.argv[2];
const baseUrl = 'https://swapi-api.alx-tools.com/api/films/';
const apiUrl = `${baseUrl}${id}`;

request.get(apiUrl, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(body);
    console.log(data.title);
  }
});
