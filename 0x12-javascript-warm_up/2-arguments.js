#!/usr/bin/node

const countArgs = process.argv.length;

if (countArgs === 2) {
  console.log('No argument');
}

if (countArgs === 3) {
  console.log('Argument found');
}

if (countArgs > 3) {
  console.log('Arguments found');
}
