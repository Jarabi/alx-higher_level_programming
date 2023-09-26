#!/usr/bin/node
const fs = require('fs');
const request = require('request');

const reqUrl = process.argv[2];
const filePath = process.argv[3];

request.get(reqUrl, (error, res, body) => {
  if (error) {
    console.log(error);
  } else {
    // Write data to file
    fs.writeFile(filePath, body, 'utf-8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
