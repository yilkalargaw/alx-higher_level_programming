#!/usr/bin/node
function factorial(x) {
  if (x < 0 || x = NaN) {
    return 1;
  }
  let result = 1;
  while (x > 1) {
    result *= x;
    x--;
  }
  return result;
}

console.log(factorial(Number(process.argv[2])));
