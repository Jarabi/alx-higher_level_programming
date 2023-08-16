#!/usr/bin/node

const dict = require('./101-data.js').dict;

// New object for user ids by occurrence
const idsByOccurrence = {};

// Array of user ids
const userIds = Object.keys(dict);

// Group the ids by occurrence
userIds.forEach(id => {
  const entry = dict[id];

  if (!idsByOccurrence[entry]) {
    // If entry doesn't exist, create array for that entry
    idsByOccurrence[entry] = [];
  }
  idsByOccurrence[entry].push(id);
});

console.log(idsByOccurrence);
