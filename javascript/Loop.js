'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });
    
    main();    
});

function readLine() {
    return inputString[currentLine++];
}

/*
 * Complete the vowelsAndConsonants function.
 * Print your output using 'console.log()'.
 */
function vowelsAndConsonants(s) {
    const vowels = "aeiou";
    let vowelString = "";
    let constantString = "";
    for(let i = 0; i < s.length; i++) {
        // cannot use concat() method, because concat() returns a new string
        if(vowels.indexOf(s.charAt(i)) != -1) vowelString += s.charAt(i);
        else constantString += s.charAt(i);
    }
    
    for(let i = 0; i < vowelString.length; i++) {
        console.log(vowelString.charAt(i));
    }
    for(let i = 0; i < constantString.length; i++) {
        console.log(constantString.charAt(i));
    }
    
}

function main() {
    const s = readLine();
    
    vowelsAndConsonants(s);
}