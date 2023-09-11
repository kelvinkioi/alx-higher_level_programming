#!/usr/bin/node
const argv = process.argv;
if (argv[2] !== undefined) {
  const temp = argv[2];
  console.log(temp);
} else {
  console.log('No argument');
}
