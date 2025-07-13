#!/usr/bin/node
const args = process.argv.slice(2).map(x => parseInt(x));

if (args.length < 2) {
  console.log(0);
} else {
  let max = Number.MIN_SAFE_INTEGER;
  let secondMax = Number.MIN_SAFE_INTEGER;

  for (const num of args) {
    if (num > max) {
      secondMax = max;
      max = num;
    } else if (num > secondMax && num < max) {
      secondMax = num;
    }
  }

  // Handle case where all numbers are equal or secondMax not updated
  if (secondMax === Number.MIN_SAFE_INTEGER) {
    console.log(0);
  } else {
    console.log(secondMax);
  }
}
