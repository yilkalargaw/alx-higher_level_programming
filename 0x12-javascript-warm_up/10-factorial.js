#!/usr/bin/node
function factorial(x) {
  var memo = {};
  function factorial(n) {
    return n < 2 ? 1 : memo[n] || (memo[n] = n * factorial(n - 1));
  }
  return factorial(x);
}

console.log(factorial(Number(process.argv[2])))
