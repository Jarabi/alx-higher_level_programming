# 0x14. JavaScript - Web scraping

<kbd>Scripting</kbd> <kbd>API</kbd> <kbd>JavaScript</kbd>

[![js-semistandard-style](https://img.shields.io/badge/code%20style-semistandard-brightgreen.svg)](https://github.com/standard/semistandard)

## General

* Why JavaScript programming is amazing?
* How to manipulate JSON data
* How to use `request` and fetch API
* How to read and write a file using `fs` module

## Tasks

<table>
<tr><th>Task</th><th>Description</th><th>Example</th></tr>
<tr>
<td>0. Readme</td>
<td>Write a script that reads and prints the content of a file.
<br>&middot; The first argument is the file path
<br>&middot; The content of the file must be read in `utf-8`
<br>&middot; If an error occurred during the reading, print the error object</td>
<td>

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

</td>
</tr>
<tr>
<td>1. Write me</td>
<td>Write a script that writes a string to a file.
<br>&middot; The first argument is the file path
<br>&middot; The second argument is the string to write
<br>&middot; The content of the file must be written in `utf-8`
<br>&middot; If an error occurred during while writing, print the error object</td>
<td>

```javascript
0x14$ ./1-writeme.js my_file.txt "Python is cool"
0x14$ cat my_file.txt ; echo ""
Python is cool
0x14$ 
```

</td>
</tr>
<tr>
<td>2. Status code</td>
<td>Write a script that display the status code of a `GET` request.
<br>&middot;The first argument is the URL to request (`GET`)
<br>The status code must be printed like this: `code: <status code>`
<br>You must use the module `request`</td>
<td>

```javascript
0x14$ ./2-statuscode.js https://alx-intranet.hbtn.io/status
code: 200
0x14$ ./2-statuscode.js https://alx-intranet.hbtn.io/doesnt_exist
code: 404
0x14$
```

</td>
</tr>
</table>
