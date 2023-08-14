#!/usr/bin/node

const argument = process.argv[2];
const number = parseInt(argument);
let f = 1;

if (isNaN(number)) {
  console.log(f);
} else {
  factorial(number);
  console.log(f);
}

function factorial (n) {
  if (n > 0) {
    f *= n;
    factorial(n - 1);
  }
}
