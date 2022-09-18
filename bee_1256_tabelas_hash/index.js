var input = require('fs').readFileSync('stdin', 'utf8');
var lines = input.split('\n');

for (i = 1; i+1 < lines.length; i += 2) {
  const nAddresses = parseInt(lines[i].split(' ')[0]);
  const numbers = lines[i + 1].split(' ').map(n => parseInt(n));
  const myHash = {};

  for(let i = 0; i < nAddresses; i++) {
    myHash[i] = [];
  }

  numbers.map((number) => {
    myHash[number % nAddresses].push(number);
  })

  Object.keys(myHash).forEach((key) => {
    process.stdout.write(`${key}`);
    myHash[key].map((number) => {
      process.stdout.write(` -> ${number}`);
    });
    console.log(` -> \\`);
  });

    console.log('');
}