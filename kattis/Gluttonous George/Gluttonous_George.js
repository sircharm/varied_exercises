//Accepted (100) - 0.04 s
//node.js

const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.on('line', (line) => {
    let numbers = line.split(' ').map(Number);
    if (numbers[0] > numbers[2]){
        console.log('>');
    }
    else if (numbers[0] < numbers[2]){
        console.log('<');
    }
    else{
        console.log('Goggi svangur!')
    }
}).on('close', () => {
    process.exit(0)
});
