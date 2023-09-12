#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let x = 0;
  for (let i = 0; i < list.length; i++) {
    list[i] === searchElement ?  x++ : x, 0;
  }
  return (x);
};
