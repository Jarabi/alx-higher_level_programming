# 0x12. JavaScript - Warm up
<kbd>Javascript</kbd>

## General
### JavaScript is amazing
JavaScript is a versatile programming language that can be used for both front-end and back-end development. It powers the interactivity of web pages, creating dynamic user experiences, and can also be used to build server-side applications using platforms like Node.js.
### Running a JavaScript script
Running a JavaScript script can be done in various environments, depending on whether you're working in a web browser, on the command line, or in other development environments:
#### Web browser
You can include JavaScript code directly within an HTML file using a `<script>` tag.
```html
<!DOCTYPE html>
<html>
<head>
    <title>JavaScript Example</title>
</head>
<body>
    <script>
        // Your JavaScript code here
        console.log("Hello, world!");
    </script>
</body>
</html>
```
#### Command line (Node.js)
If you want to run JavaScript code outside of a web browser, you can use Node.js, a runtime that allows you to execute JavaScript on the command line or server-side. Here's how to run a JavaScript script using Node.js:
- First, make sure you have Node.js installed on your computer.
- Create a JavaScript file (e.g., `myscript.js`) and add your code to it.
- Open your command-line interface and navigate to the directory where your script is located.
- Run the script using the `node` command:
```bash
node myscript.js
```
#### Integrated Development Environments (IDEs):
If you're using an integrated development environment, you can create a JavaScript file and run it directly from the IDE.
### Creating variables and constants
Variables are used to store values that can change, while constants store values that should remain constant throughout the program's execution.
#### Variables:
To create a variable, use the `var`, `let`, or `const` keyword, followed by the variable name. The recommended practice is to use `let` or `const` as they provide better scoping rules than `var`.
```javascript
// Using let (block-scoped)
let age = 25;
let name = "John";

// Using const (block-scoped and cannot be reassigned)
const pi = 3.14159;
```
Variables created with `let` can be updated with new values:
```javascript
let count = 10;
count = count + 1; // Increment count by 1
```
#### Constants:
Constants are declared using the `const` keyword. They cannot be reassigned after their initial assignment.
```javascript
const appName = "MyApp";
const gravity = 9.81;
```
Attempting to reassign a constant will result in an error:
```javascript
const maxUsers = 100;
maxUsers = 150; // This will result in an error
```
It's important to note that the choice between using `let` and `const` depends on whether the value of the variable will change over time. If the value needs to remain constant, use `const`. If the value might change, use `let`.


4.  What are differences between `var`, `const` and `let`
5.  What are all the data types available in JavaScript
6.  How to use the `if`, `if ... else` statements
7.  How to use comments
8.  How to affect values to variables
9.  How to use `while` and `for` loops
10. How to use `break` and `continue` statements
11. What is a function and how do you use functions
12. What does a function that does not use any `return` statement return
13. Scope of variables
14. What are the arithmetic operators and how to use them
15. How to manipulate dictionary
16. How to import a file

## Scripts

| Name | Description |
|------|-------------|
| [0-javascript\_is\_amazing.js](https://github.com/Jarabi/alx-higher_level_programming/blob/main/0x12-javascript-warm_up/0-javascript_is_amazing.js) | Prints "JavaScript is amazing" |
| [1-multi\_languages.js](https://github.com/Jarabi/alx-higher_level_programming/blob/main/0x12-javascript-warm_up/1-multi_languages.js) | Prints 3 lines. |
| [2-arguments.js](https://github.com/Jarabi/alx-higher_level_programming/blob/main/0x12-javascript-warm_up/2-arguments.js) | Prints a message depending of the number of arguments passed. |
| [3-value\_argument.js](https://github.com/Jarabi/alx-higher_level_programming/blob/main/0x12-javascript-warm_up/3-value_argument.js) | Prints the first argument passed to it. |
| [4-concat.js](https://github.com/Jarabi/alx-higher_level_programming/blob/main/0x12-javascript-warm_up/4-concat.js) | Prints two arguments passed to it, in the following format: “ is ” |
| [5-to\_integer.js](https://github.com/Jarabi/alx-higher_level_programming/blob/main/0x12-javascript-warm_up/5-to_integer.js) | Prints My number: \<first argument converted in integer\> if the first argument can be converted to an integer. |
| [6-multi\_languages\_loop.js](https://github.com/Jarabi/alx-higher_level_programming/blob/main/0x12-javascript-warm_up/6-multi_languages_loop.js) | Prints 3 lines: (like 1-multi\_languages.js) but by using an array of string and a loop. |
| [7-multi\_c.js](https://github.com/Jarabi/alx-higher_level_programming/blob/main/0x12-javascript-warm_up/7-multi_c.js) | Prints x times “C is fun” |
| [8-square.js](https://github.com/Jarabi/alx-higher_level_programming/blob/main/0x12-javascript-warm_up/8-square.js) | Prints a square. |
| [9-add.js](https://github.com/Jarabi/alx-higher_level_programming/blob/main/0x12-javascript-warm_up/9-add.js) | Prints the addition of 2 integers. |
| [10-factorial.js](https://github.com/Jarabi/alx-higher_level_programming/blob/main/0x12-javascript-warm_up/10-factorial.js) | Computes and prints a factorial. |
| [11-second\_biggest.js](https://github.com/Jarabi/alx-higher_level_programming/blob/main/0x12-javascript-warm_up/11-second_biggest.js) | Searches the second biggest integer in the list of arguments. |
| [12-object.js](https://github.com/Jarabi/alx-higher_level_programming/blob/main/0x12-javascript-warm_up/12-object.js) | Replaces the value 12 with 89. |
| [13-add.js](https://github.com/Jarabi/alx-higher_level_programming/blob/main/0x12-javascript-warm_up/13-add.js) | Returns the addition of 2 integers. |
| [100-let\_me\_const.js](https://github.com/Jarabi/alx-higher_level_programming/blob/main/0x12-javascript-warm_up/100-let_me_const.js) | Modifies the value of myVar to 333. |
| [101-call\_me\_moby.js](https://github.com/Jarabi/alx-higher_level_programming/blob/main/0x12-javascript-warm_up/101-call_me_moby.js) | Executes x times a function. |
| [102-add\_me\_maybe.js](https://github.com/Jarabi/alx-higher_level_programming/blob/main/0x12-javascript-warm_up/102-add_me_maybe.js) | Increments and calls a function. |
| [103-object\_fct.js](https://github.com/Jarabi/alx-higher_level_programming/blob/main/0x12-javascript-warm_up/103-object_fct.js) | Adds a new function incr that increments the integer value. |

## Usage:

### 0-javascript\_is\_amazing.js
Prints `JavaScript is amazing`:
```javascript
0x12$ ./0-javascript_is_amazing.js 
JavaScript is amazing
0x12$ 
0x12$ semistandard ./0-javascript_is_amazing.js 
0x12$
```
### 1-multi\_languages.js
Prints 3 lines:
- The first line: `C is fun`
- The second line: `Python is cool`
- The third line: `JavaScript is amazing`
```javascript
0x12$ ./1-multi_languages.js 
C is fun
Python is cool
JavaScript is amazing
0x12$
```
### 2-arguments.js
Prints a message depending of the number of arguments passed:
- If no arguments are passed to the script, print `No argument`
- If only one argument is passed to the script, print `Argument found`
- Otherwise, print `Arguments found`
```javascript
0x12$ ./2-arguments.js 
No argument
0x12$ ./2-arguments.js Best
Argument found
0x12$ ./2-arguments.js Best School
Arguments found
0x12$
```
### 3-value\_argument.js
Prints the first argument passed to it:
- If no arguments are passed to the script, print `No argument`
```javascript
0x12$ ./3-value_argument.js 
No argument
0x12$ ./3-value_argument.js School
School
0x12$
```
### 4-concat.js
Prints two arguments passed to it, in the following format: `<first> is <second>`
```javascript
0x12$ ./4-concat.js c cool
c is cool
0x12$ ./4-concat.js c 
c is undefined
0x12$ ./4-concat.js
undefined is undefined
0x12$
```
### 5-to\_integer.js
Prints `My number: <first argument converted to integer>` if the first argument can be converted to an integer:
- If the argument can’t be converted to an integer, print `Not a number`
```javascript
0x12$ ./5-to_integer.js 
Not a number
0x12$ ./5-to_integer.js 89
My number: 89
0x12$ ./5-to_integer.js "89"
My number: 89
0x12$ ./5-to_integer.js 89.89
My number: 89
0x12$ ./5-to_integer.js School
Not a number
0x12$
```
### 6-multi\_languages\_loop.js
Prints 3 lines: (like 1-multi\_languages.js) but by using an array of string and a loop
- The first line: `C is fun`
- The second line: `Python is cool`
- The third line: `JavaScript is amazing`
```javascript
0x12$ ./6-multi_languages_loop.js 
C is fun
Python is cool
JavaScript is amazing
0x12$
```
### 7-multi\_c.js
Prints x times `C is fun`:
- where `x` is the first argument of the script
- If the first argument can’t be converted to an integer, print `Missing number of occurrences`
```javascript
0x12$ ./7-multi\_c.js 2
C is fun
C is fun
0x12$ ./7-multi\_c.js 5
C is fun
C is fun
C is fun
C is fun
C is fun
0x12$ ./7-multi\_c.js 
Missing number of occurrences
0x12$ ./7-multi\_c.js -3
0x12$
```
### 8-square.js
Prints a square:
- The first argument is the size of the square
- If the first argument can’t be converted to an integer, print `Missing size`
- You must use the character `X` to print the square
```javascript
0x12$ ./8-square.js
Missing size
0x12$ ./8-square.js School
Missing size
0x12$ ./8-square.js 2
XX
XX
0x12$ ./8-square.js 6
XXXXXX
XXXXXX
XXXXXX
XXXXXX
XXXXXX
XXXXXX
0x12$ ./8-square.js -3
0x12$ 
```
### 9-add.js
Prints the addition of 2 integers
- The first argument is the first integer
- The second argument is the second integer
```javascript
0x12$ ./9-add.js 
NaN
0x12$ ./9-add.js 1
NaN
0x12$ ./9-add.js 1 7
8
0x12$ ./9-add.js 13 89
102
0x12$
```
### 10-factorial.js
Computes and prints a factorial:
- The first argument is integer (argument can be cast as integer) used for computing the factorial
- Factorial of `NaN` is 1
```javascript
0x12$ ./10-factorial.js 
1
0x12$ ./10-factorial.js 3
6
0x12$ ./10-factorial.js 89
1.6507955160908452e+136
0x12$ ./10-factorial.js 333
Infinity
0x12$ 
```
### 11-second\_biggest.js
Searches the second biggest integer in the list of arguments.
- If no argument passed, print 0
- If the number of arguments is 1, print 0
```javascript
0x12$ ./11-second_biggest.js 
0
0x12$ ./11-second_biggest.js 1
0
0x12$ ./11-second_biggest.js 4 2 5 3 0 -3
4
0x12$
```
### 12-object.js
Replaces the value 12 with 89
```javascript
0x12$ ./12-object.js
{ type: 'object', value: 12 }
{ type: 'object', value: 89 }
0x12$
```
### 13-add.js
Returns the addition of 2 integers
```javascript
0x12$ cat 13-main.js
#!/usr/bin/node
const add = require('./13-add').add;
console.log(add(3, 5));
0x12$ ./13-main.js
8
0x12$
```
### 100-let\_me\_const.js
Modifies the value of `myVar` to 333
```javascript
0x12$ cat 100-main.js
#!/usr/bin/node
myVar = 89;
require('./100-let_me_const')
console.log(myVar);
0x12$ ./100-main.js
333
0x12$
```
### 101-call\_me\_moby.js
Executes `x` times a function
```javascript
0x12$ cat 101-main.js
#!/usr/bin/node
const callMeMoby = require('./101-call_me_moby').callMeMoby;
callMeMoby(3, function () {
  console.log('C is fun');
});
0x12$ ./101-main.js
C is fun
C is fun
C is fun
0x12$
```
### 102-add\_me\_maybe.js
Increments and calls a function
```javascript
0x12$ cat 102-main.js
#!/usr/bin/node
const addMeMaybe = require('./102-add_me_maybe').addMeMaybe;
addMeMaybe(4, function (nb) {
  console.log('New value: ' + nb);
});
0x12$ ./102-main.js
New value: 5
0x12$
```
### 103-object\_fct.js
Adds a new function `incr` that increments the integer `value`
```javascript
0x12$ cat 103-object_fct.js
#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
/*
YOUR CODE HERE
*/
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);

0x12$ ./103-object_fct.js 
{ type: 'object', value: 12 }
{ type: 'object', value: 13, incr: [Function] }
{ type: 'object', value: 14, incr: [Function] }
{ type: 'object', value: 15, incr: [Function] }
0x12$
```
&copy; Alex Jarabi &middot; 2023
