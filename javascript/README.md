## How to ues Node.js run JavaScript Code Without Browser  
Quoted from : https://boostlog.io/@adamolly/nodejs-run-javascript-code-without-a-browser-5aa0e52ae922f1008c7efbe7  
npm init  
node JavaScriptFileName.js  
## Identifiers  
Quoted from : https://www.hackerrank.com/challenges/js10-hello-world/topics    
A JavaScript identifier must begin with a letter, an underscore (_), or a dollar sign ($). Subsequent characters can be letters, underscores, dollar signs, or digits (i.e., the numbers  through ).  
~~~~
// Some valid identifiers are:
x
variable_name
sum13
_variable
$variable
~~~~
## Optional Semicolon  
Quoted from : https://www.hackerrank.com/challenges/js10-hello-world/topics   
Like many programming languages, JavaScript uses the semicolon (;) to separate statements from each other. This is important as it makes the meaning of your code clear; without a separator, the end of one statement might appear to be the beginning of the next (and vice versa). In JavaScript, you can usually omit the semicolon between two statements as long as those statements are written on separate lines.
## Data Types  
Quoted from : https://www.hackerrank.com/challenges/js10-data-types/topics  

## Arrays for...in statement and for...of statement  
Quoted from : https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Loops_and_iteration  
The following example shows the difference between a for...of loop and a for...in loop. While for...in iterates over property names, for...of iterates over property values:
~~~~
var arr = [3, 5, 7];
arr.foo = 'hello';

for (var i in arr) {
   console.log(i); // logs "0", "1", "2", "foo"
}

for (var i of arr) {
   console.log(i); // logs 3, 5, 7
}
~~~~