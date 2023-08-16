#!/usr/bin/node

const list = require('./100-data.js').list;

const newList = list.map((el, idx) => idx * el);
console.log(list);
console.log(newList);
