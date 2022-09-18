var input = require('fs').readFileSync('stdin', 'utf8');
var lines = input.split('\n');

for(let i = 0; i < lines.length; i++) {
  const number = parseInt(lines[i]);
  if(!!number) {
    const deck = [];
    const discarded = [];

    for(j = 0; j < number; j++) {
      deck.push(j+1);
    }

    while(deck.length > 1) {
      discarded.push(deck.shift());
      deck.push(deck.shift());
    }

    process.stdout.write('Discarded cards:');
    for(j = 0; j < discarded.length; j++) {
      process.stdout.write(` ${discarded[j]}`);
      if(j < discarded.length - 1) {
        process.stdout.write(',');
      } 
    }
    console.log('');

    console.log(`Remaining card: ${deck[0]}`);
  }
}