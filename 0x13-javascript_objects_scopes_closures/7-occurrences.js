#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  const count = list.filter(el => el === searchElement);
  return count.length;
};
