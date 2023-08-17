# 0x12. JavaScript - Warm up
<kbd>Javascript</kbd>

## General
### JavaScript is amazing
JavaScript is a versatile programming language that can be used for both front-end and back-end development. It powers the interactivity of web pages, creating dynamic user experiences, and can also be used to build server-side applications using platforms like Node.js.
---
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
---
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
---
### JavaScript Datatypes
Here are the main data types available in JavaScript:
#### Primitive Data Types:
- __Number__: Represents both integer and floating-point numbers.
- __String__: Represents sequences of characters, such as text.
- __Boolean__: Represents true or false values.
- __Undefined__: Represents a variable that has been declared but hasn't been assigned a value.
- __Null__: Represents the intentional absence of any value.
- __Symbol__: Represents a unique and immutable value, often used as object property keys.
- __BigInt__: Represents integers of arbitrary precision (introduced in ECMAScript 2020).
#### Complex Data Types:
- __Object__: Represents a collection of key-value pairs. Objects can hold various types of data and functions. This includes built-in objects like arrays, functions, and dates, as well as custom objects.
- __Array__: Represents an ordered list of values, which can be of any data type.
- __Function__: Represents executable code and can be defined using function expressions or function declarations.
- __Date__: Represents dates and times.
- __RegExp__: Represents regular expressions, used for pattern matching within strings.

JavaScript is dynamically typed, meaning you don't need to explicitly specify a data type when declaring a variable. The data type is determined automatically based on the value assigned to the variable. Additionally, JavaScript has a feature called type coercion, where values can be automatically converted from one type to another in certain contexts.

Examples:
```javascript
// Primitive data types
let age = 30;                // Number
let name = "Alice";          // String
let isStudent = true;        // Boolean
let notDefined;              // Undefined
let noValue = null;          // Null
let uniqueSymbol = Symbol(); // Symbol

// Complex data types
let person = {              // Object
    firstName: "John",
    lastName: "Doe"
};

let numbers = [1, 2, 3];    // Array

function greet() {          // Function
    console.log("Hello!");
}

let today = new Date();     // Date

let pattern = /abc/;        // RegExp
```
---
### if, if ... else statements
In JavaScript, the if and if...else statements are used for conditional execution of code. They allow you to make decisions based on whether a given condition evaluates to `true` or `false`.  Examples:
```javascript
let age = 15;

if (age >= 18) {
    console.log("You are an adult.");
} else {
    console.log("You are not yet an adult.");
}
```
---
### How to use comments
In JavaScript, comments are used to add explanatory notes or annotations to your code. Comments are ignored by the JavaScript interpreter and are not executed as part of the program.
#### Single-line Comments:
Single-line comments are used to add comments to a single line of code. Anything after the comment indicator `//` on a line is treated as a comment and is not executed by the JavaScript interpreter.
```javascript
// This is a single-line comment
let age = 25; // This comment explains the purpose of the variable
```
#### Multi-line Comments:
Multi-line comments, also known as block comments, are used to write comments that span multiple lines. These comments are enclosed within `/*` and `*/`, and any text between them is treated as a comment.
```javascript
/*
This is a multi-line comment.
It can span multiple lines.
*/

let firstName = "John";
/* This comment explains that the variable stores a person's first name */
let lastName = "Doe";
```
Comments are a valuable tool for improving code readability and maintainability.
---
### How to affect values to variables
When assigning values to variables, you should keep in mind a few important points:
1. __Initialization__: When declaring a variable, you can assign an initial value to it. For example, `let age = 30;`. This is called variable initialization.
2. __Changing Values__: Variables can have their values changed after they have been assigned. For instance, `age = 31`; would update the value of the `age` variable to 31.
3. __Data Types__: Variables can hold values of different data types, such as numbers, strings, boolean values, and more. Make sure the value you assign matches the intended data type.
4. __Reassignment__: You can assign a new value to a variable that already holds a value. This will replace the old value with the new one.
5. __Scope__: The scope of a variable determines where it can be accessed and modified. Variables declared with __let__ and __const__ are block-scoped, meaning they are limited to the block (usually enclosed by curly braces `{}`) in which they are defined.
6. __Hoisting__: Variables declared with `var` are hoisted to the top of their scope during the compilation phase, which means you can use them before they are declared. However, it's considered a best practice to declare your variables before using them.
---
### How to use while and for loops
In JavaScript, loops are used to repeatedly execute a block of code until a certain condition is met. Two common types of loops are the `while` loop and the `for` loop.
#### while Loop:
The `while` loop continues executing a block of code as long as a specified condition is `true`. Example:
```javascript
let sum = 0;
let num = 1;

while (num <= 10) {
    sum += num;
    num++;
}

console.log(sum); // Output: 55 (1 + 2 + ... + 10)
```
#### for Loop:
The `for` loop provides a more compact way to create loops, especially when you know the number of iterations beforehand. The `for` loop consists of three parts: initialization, condition, and iteration. Example:
```javascript
let sum = 0;

for (let num = 1; num <= 10; num++) {
    sum += num;
}

console.log(sum); // Output: 55
```
Both while and for loops are essential constructs in programming and can greatly enhance the efficiency and functionality of your code.
---
### How to use break and continue statements
In JavaScript, the `break` and `continue` statements are used within loops to control the flow of execution. They provide ways to terminate the current iteration of a loop (`continue`) or completely exit the loop (`break`).
#### break Statement:
The `break` statement is used to exit the current loop prematurely when a certain condition is met. When the `break` statement is encountered, the loop terminates immediately, and the program continues executing after the loop. Example:
```javascript
const numbers = [1, 3, 4, 5, 6, 7, 8, 9, 10];

for (let i = 0; i < numbers.length; i++) {
    if (numbers[i] % 2 === 0) {
        console.log("Found the first even number:", numbers[i]);
        break; // Exit the loop
    }
}
```
#### continue Statement:
The `continue` statement is used to skip the rest of the current iteration of a loop and move to the next iteration. This can be useful when you want to skip processing certain items in an array or other iterable. Example:
```javascript
const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

for (let i = 0; i < numbers.length; i++) {
    if (numbers[i] % 2 !== 0) {
        continue; // Skip odd numbers and move to the next iteration
    }
    console.log("Even number:", numbers[i]);
}
```
---
### Functions and how to use them
A function in JavaScript is a reusable block of code that performs a specific task or set of tasks. Functions are used to modularize code, improve code organization, and promote reusability. They allow you to encapsulate a piece of functionality and call it whenever you need it. Functions can accept inputs (arguments) and produce outputs (return values). Example:
```javascript
// Function declaration
function greet(name) {
    console.log("Hello, " + name + "!");
}

// Function call
greet("Alice"); // Output: Hello, Alice!
greet("Bob");   // Output: Hello, Bob!
```
You can also create functions that return values:
```javascript
function add(a, b) {
    return a + b;
}

let result = add(5, 3);
console.log(result); // Output: 8
```
> [!NOTE]
> A function that does not contain a `return` statement explicitly will return the value `undefined` by default. This means that when the function is called and executed, if no return statement is encountered, the function will still return the value `undefined` to the caller. Example:
```javascript
function greet(name) {
    console.log("Hello, " + name + "!");
}

let result = greet("Alice"); // Output: Hello, Alice!
console.log(result); // Output: undefined
```
---
### Scope of variables
In JavaScript, the scope of a variable defines where in your code that variable can be accessed or modified. The scope of a variable is determined by where it is declared, and it affects how that variable can be used within your program. There are two main types of scope in JavaScript: global scope and local scope.
#### Global Scope:
A variable declared outside of any function or code block has global scope. It can be accessed from anywhere in the code, both inside and outside functions.
```javascript
let globalVariable = 10;

function myFunction() {
    console.log(globalVariable); // Accessing global variable inside the function
}

console.log(globalVariable); // Accessing global variable outside the function
```
#### Local Scope:
Variables declared inside a function or code block have local scope. They are accessible only within that function or block.
```javascript
function myFunction() {
    let localVariable = 20; // Local variable
    console.log(localVariable); // Accessing local variable inside the function
}

// console.log(localVariable); // This would result in an error, as localVariable is not accessible here
```
__Block Scope__:
In modern JavaScript (ES6 and later), variables declared with `let` and `const` have block scope, which means they are limited to the block (portion of code enclosed by curly braces {}) in which they are declared.
```javascript
if (true) {
    let blockScopedVariable = 30;
    const anotherBlockScopedVariable = 40;
}

// console.log(blockScopedVariable); // This would result in an error
// console.log(anotherBlockScopedVariable); // This would also result in an error
```
---
### Arithmetic operators and how to use them
Arithmetic operators in JavaScript are used to perform mathematical calculations on numerical values. Here are the main arithmetic operators and how to use them:
#### 1. Addition +:
The addition operator is used to add two numbers together.
```javascript
let sum = 5 + 3; // Result: 8
```
#### 2. Subtraction -:
The subtraction operator is used to subtract one number from another.
```javascript
let difference = 10 - 4; // Result: 6
```
#### 3. Multiplication *:
The multiplication operator is used to multiply two numbers.
```javascript
let product = 3 * 6; // Result: 18
```
#### 4. Division /:
The division operator is used to divide one number by another.
```javascript
let quotient = 20 / 5; // Result: 4
```
#### 5. Modulus %:
The modulus operator returns the remainder of a division operation.
```javascript
let remainder = 10 % 3; // Result: 1 (10 divided by 3 leaves a remainder of 1)
```
#### 6. Exponentiation ** (ES6):
The exponentiation operator calculates the power of a number.
```javascript
let result = 2 ** 3; // Result: 8 (2 raised to the power of 3)
```
---
### Manipulating dictionaries
In JavaScript, dictionaries are known as objects. Objects are a fundamental data structure that allow you to store and organize data as key-value pairs.
####  Creating an Object:
You can create an object by using curly braces `{}` and specifying key-value pairs within the object.
```javascript
let person = {
    firstName: "John",
    lastName: "Doe",
    age: 30,
    isStudent: false
};
```
#### Accessing Values:
You can access values in an object using dot notation or bracket notation.
```javascript
console.log(person.firstName); // Output: John
console.log(person["lastName"]); // Output: Doe
```
#### Modifying Values:
You can modify values in an object by assigning new values to the corresponding keys.
```javascript
person.age = 31;
person["isStudent"] = true;
```
#### Adding New Key-Value Pairs:
You can add new key-value pairs to an object by assigning a value to a new key.
```javascript
person.country = "USA";
```
#### Removing Key-Value Pairs:
You can remove key-value pairs from an object using the `delete` keyword.
```javascript
delete person.isStudent;
```
#### Iterating Over Object Properties:
You can loop through an object's properties using a `for...in` loop.
```javascript
for (let key in person) {
    console.log(key + ": " + person[key]);
}
```
#### Checking if a Key Exists:
You can check if a specific key exists in an object using the `hasOwnProperty()` method.
```javascript
if (person.hasOwnProperty("age")) {
    console.log("Age exists in the object.");
}
```
#### Object Methods and Functions:
Objects can also have functions as values, which are known as methods. Methods can perform actions related to the object's data.
```javascript
let calculator = {
    add: function(a, b) {
        return a + b;
    },
    subtract: function(a, b) {
        return a - b;
    }
};

console.log(calculator.add(5, 3)); // Output: 8
console.log(calculator.subtract(10, 5)); // Output: 5
```
---
### Importing files
In JavaScript, there are different methods to import code from other files, depending on the context in which you're working. The method you use depends on the environment you're working in, such as browsers, Node.js, or modern ES6 modules.
#### 1. Browser Environment:
In the browser, you can use the HTML `<script>` tag to include external JavaScript files. Just provide the src attribute with the path to the file you want to import.
```html
<script src="path/to/your-script.js"></script>
```
The contents of `your-script.js` will be included and executed in the order specified.
#### 2. Node.js Environment:
In Node.js, you can use the `require()` function to import code from other files.
Suppose you have a file named `utils.js`:
```javascript
// utils.js
function sayHello() {
    console.log("Hello from utils.js");
}

module.exports = {
    sayHello: sayHello
};
```
In another file, you can import the `sayHello` function:
```javascript
const utils = require('./utils');
utils.sayHello(); // Output: Hello from utils.js
```
#### 3. ES6 Modules (Modern Approach):
ES6 introduced a standardized module system for JavaScript. You can use the `import` and `export` keywords to work with modules.
Suppose you have a file named `utils.js`:
```javascript
// utils.js
export function sayHello() {
    console.log("Hello from utils.js");
}
```
In another file, you can import the `sayHello` function:
```javascript
import { sayHello } from './utils';
sayHello(); // Output: Hello from utils.js
```

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
