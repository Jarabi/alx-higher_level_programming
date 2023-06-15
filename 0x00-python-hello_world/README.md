# 0x00. Python - Hello, World

## General

1. Why Python programming is awesome?
Python is an easy to learnm yet powerful programming language, with an effective approach to object-oriented programming.

2. Who created Python?
Guido van Rossum

3. Who is Guido van Rossum?
Guido van Rossum is a Dutch computer programmer and author.

4. Where does the name ‘Python’ come from?
The name 'Python' comes from the BBC show 'Monty Python's Flying Circus.

5. What is the Zen of Python?
The Zen of Python, by Tim Peters

> Beautiful is better than ugly.
> Explicit is better than implicit.
> Simple is better than complex.
> Complex is better than complicated.
> Flat is better than nested.
> Sparse is better than dense.
> Readability counts.
> Special cases aren't special enough to break the rules.
> Although practicality beats purity.
> Errors should never pass silently.
> Unless explicitly silenced.
> In the face of ambiguity, refuse the temptation to guess.
> There should be one-- and preferably only one --obvious way to do it.
> Although that way may not be obvious at first unless you're Dutch.
> Now is better than never.
> Although never is often better than *right* now.
> If the implementation is hard to explain, it's a bad idea.
> If the implementation is easy to explain, it may be a good idea.
> Namespaces are one honking great idea -- let's do more of those!

6. How to use the Python interpreter:
Putting /usr/local/bin in your Unix shell’s search path makes it possible to start it by typing the command:
`$ python3.11`

Typing the end-of-line character (CTRL-D) at the primary prompt causes the interpretter to exit with a zero status.
Alternatively, you can use command `quit()`

A second way to start the interpretter is `python -c command [arg] ...` which executes the statements in `command`.

7. How to print text and variables using **print**
Python three alternatives to print text and variables:

### Option #1: %-formatting
String objects have a built-in operation using the `%` operator, which you can use to format strings.
Here’s what that looks like in practice:
```
>>> name = "Alex"
>>> print("Hello, %s." % name)
'Hello, Alex.'
```
In order to insert more than one variable, you must use a tuple of those variables. Here’s how you would do that:
```
>>> name = "Alex"
>>> age = 40
>>> print("Hello, %s. You are %s." % (name, age))
'Hello, Alex. You are 40.'
```
With %-formatting, however, once you start using several parameters and longer strings, your code will quickly become
much less easily readable.

### Option #2: str.format()
Introduced in Python 2.6, str.format()  is an improvement on %-formatting. With str.format(), the replacement fields
are marked by curly braces:
```
>>> print("Hello, {}. You are {}.".format(name, age))
'Hello, Alex. You are 40.'
```
You can reference variables in any order by referencing their index:
```
>>> print("Hello, {1}. You are {0}.".format(age, name))
'Hello, Alex. You are 40.'
```
But if you insert the variable names, you get the added perk of being able to pass objects and then reference parameters
and methods in between the braces:
```
>>> person = {'name': 'Alex', 'age': 40}
>>> print("Hello, {name}. You are {age}.".format(name=person['name'], age=person['age']))
'Hello, Alex. You are 40.'
```
You can also use ** to do this neat trick with dictionaries:
```
>>> print("Hello, {name}. You are {age}.".format(**person))
'Hello, Alex. You are 40.'
```

### f-Strings: A New and Improved Way to Format Strings in Python
The syntax is similar to the one you used with str.format() but less verbose. Look at how easily readable this is:
`>>> print(f"Hello, {name}. You are {age}.")`

8. How to use strings:
Strings can be enclosed in single ('...') or double ("...") quotes. '\' can be used to escape quotes.
If you don't want characters prefaced with '\' to be interpretted as special characters (like '\n'), you can use raw
strings by adding an 'r' before the quote. Example:
```
>>> print('C:\some\name')  # here \n means newline!
C:\some
ame

>>> print(r'C:\some\name')  # note the r before the quote
C:\some\name
```
You can also use string literals to span multiple lines using triple-quotes: """...""" or '''...'''. Example:
```
>>> print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")
```
produces the following output (note that the initial newline is not included):
```
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
```
9. What are indexing and slicing in Python?
Strings are indexed with the first character having with index 0, starting from the left. Indices may also be negative
numbers starting from the right, beginning with -1.

Slicing allows you to obtain a substring. For example:
```
>>> word = 'Python'
>>> word[0:2]  # characters from position 0 (included) to 2 (excluded)
'Py'

>>> word[2:5]  # characters from position 2 (included) to 5 (excluded)
'tho'
```
Slice indices have useful defaults; an omitted first index defaults to zero, an omitted second index defaults to the size
of the string being sliced.

10. What is the official Python coding style and how to check your code with **pycodestyle**
The official Python coding style is pycodestyle (formerly called pep8)

Usage:
------
`$ pycodestyle --first file.py`

You can also make pycodestyle.py show the source code for each error, and even the relevant text from PEP 8:
`$ pycodestyle --show-source --show-pep8 testsuite/E40.py`

Or you can display how often each error was found:
`$ pycodestyle --statistics -qq Python-2.5/Lib`
