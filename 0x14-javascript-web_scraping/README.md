# 0x14. JavaScript - Web scraping

<kbd>Scripting</kbd> <kbd>API</kbd> <kbd>JavaScript</kbd>

[![js-semistandard-style](https://img.shields.io/badge/code%20style-semistandard-brightgreen.svg)](https://github.com/standard/semistandard)

## General

* Why JavaScript programming is amazing?
* How to manipulate JSON data
* How to use `request` and fetch API
* How to read and write a file using `fs` module

## Tasks

### 0. Readme

A script that reads and prints the content of a file.
* The first argument is the file path
* The content of the file must be read in `utf-8`
* If an error occurred during the reading, print the error object

```javascript
0x14$ cat cisfun
C is super fun!
0x14$ ./0-readme.js cisfun
C is super fun!

0x14$ ./0-readme.js doesntexist
{ Error: ENOENT: no such file or directory, open 'doesntexist'
    at Error (native)
  errno: -2,
  code: 'ENOENT',
  syscall: 'open',
  path: 'doesntexist' }
0x14$
```

### 1. Write me

A script that writes a string to a file.
* The first argument is the file path
* The second argument is the string to write
* The content of the file must be written in `utf-8`
* If an error occurred during while writing, print the error object

```javascript
0x14$ ./1-writeme.js my_file.txt "Python is cool"
0x14$ cat my_file.txt ; echo ""
Python is cool
0x14$ 
```

### 2. Status code
A script that display the status code of a `GET` request.
* The first argument is the URL to request (`GET`)
* The status code must be printed like this: `code: <status code>`
* You must use the module `request`

```javascript
0x14$ ./2-statuscode.js https://alx-intranet.hbtn.io/status
code: 200
0x14$ ./2-statuscode.js https://alx-intranet.hbtn.io/doesnt_exist
code: 404
0x14$
```
