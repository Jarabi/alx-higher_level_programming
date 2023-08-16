#!/usr/bin/node
const fs = require('fs');

const files = process.argv.slice(2);
const fileA = files[0];
const fileB = files[1];
const dest = files[2];

// Read file contents
const readFile = (file) => {
  fs.readFile(file, (err, content) => {
    if (err) {
      console.log('Read error:', err);
    }

    // Append contents to file
    fs.appendFile(dest, content, 'utf-8', (err) => {
      if (err) {
        console.log('Write error:', err);
      }
    });
  });
};

readFile(fileA);
readFile(fileB);
