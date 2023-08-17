# 0x12. JavaScript - Warm up
<kbd>Javascript</kbd>

## General
1.  Why JavaScript programming is amazing
2.  How to run a JavaScript script
3.  How to create variables and constants
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

0-javascript\_is\_amazing.js

```javascript
0x12$ ./0-javascript_is_amazing.js 
JavaScript is amazing
0x12$ 
0x12$ semistandard ./0-javascript_is_amazing.js 
0x12$ 
```
---
1-multi\_languages.js
```javascript
0x12$ ./1-multi_languages.js 
C is fun
Python is cool
JavaScript is amazing
0x12$ 
```
---
2-arguments.js
```javascript
0x12$ ./2-arguments.js 
No argument
0x12$ ./2-arguments.js Best
Argument found
0x12$ ./2-arguments.js Best School
Arguments found
0x12$
```
---
3-value\_argument.js
```javascript
0x12$ ./3-value_argument.js 
No argument
0x12$ ./3-value_argument.js School
School
0x12$ 
```
---
4-concat.js
```javascript
0x12$ ./4-concat.js c cool
c is cool
0x12$ ./4-concat.js c 
c is undefined
0x12$ ./4-concat.js
undefined is undefined
0x12$ 
```
---
5-to\_integer.js
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
