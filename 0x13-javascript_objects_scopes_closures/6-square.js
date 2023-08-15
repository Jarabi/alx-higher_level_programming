#!/usr/bin/node

const BaseSquare = require('./5-square.js');

class Square extends BaseSquare {
  charPrint (c = 'X') {
    for (let r = 0; r < this.height; r++) {
      let row = '';
      for (let col = 0; col < this.width; col++) {
        row += c;
      }
      console.log(row);
    }
  }
}

module.exports = Square;
