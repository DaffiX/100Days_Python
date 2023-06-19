
# 0x00-python-hello_world

100 Days of Learning Python with problem solving technique as a software engineer 


## Lessons

To master the language you need to understand the basics:

0.  Write a script that run the Pyhton script

```bash
#!/bin/bash

# Set the value of PYFILE o the Python file name - so you may reference that in the future

export PYFILE="pycode.py"

# Run the Python script - which is passed as arg

python3 "$PYFILE"

```

1. Run inline: Write a Shell script that runs Python code.

The Python code will be saved in the environment variable $PYCODE
The python3 -c command is used to run the Python code specified in the $PYCODE environment variable. The -c flag tells the Python interpreter to execute the code provided as a command-line argument.
```bash 
#!/bin/bash
export PYCODE="print('This is printed')"

# Run the Python code stored in the PYCODE environment variable
python3 -c "$PYCODE"
```
2. Hello, print: Python script that prints exactly "Programming is like building a multilingual puzzle, followed by a new line.

```python
$./2-print.py 
Programming is like building a multilingual puzzle
```
3. Print integer: Complete this source code in order to print the integer stored in the variable number, followed by Battery street, followed by a new line.

- You can find the source code [here](https://github.com/alx-tools/0x00.py/blob/master/3-print_number.py)
- The output of the script should be:
- the number, followed by Battery street,followed by a new line
- You are not allowed to cast the variable number into a string
- Your code must be 3 lines long
- You have to use f-strings tips

```
$ ./3-print_number.py
98 Battery street
```

4. Print Formated number: Complete the source code in order to print the float stored in the variable number with a precision of 2 digits.
```
$ ./4-print_float.py
Float: 3.14
```

5.  Print string: Complete this source code in order to print 3 times a string stored in the variable str, followed by its first 9 characters.

You can find the source code here
The output of the program should be:
- 3 times the value of str
- followed by a new line
- followed by the 9 first characters of str
- followed by a new line
- You are not allowed to use any loops or conditional statement
- Your program should be maximum 5 lines long
```
$ ./5-print_string.py 
Holberton SchoolHolberton SchoolHolberton School
Holberton
```

6. Play with strings
Complete [this source code](https://github.com/alx-tools/0x00.py/blob/master/6-concat.py) to print Welcome to Holberton School!

- You can find the source code here
- You are not allowed to use any loops or conditional statements.
- You have to use the variables str1 and str2 in your new line of code
- Your program should be exactly 5 lines long
```linux 
$ ./6-concat.py
Welcome to Holberton School!
$ wc -l 6-concat.py
5 6-concat.py
```

7. Copy - Cut - Paste
Complete [this source code](https://github.com/alx-tools/0x00.py/blob/master/7-edges.py)

- You can find the source code here
- You are not allowed to use any loops or conditional statements
- Your program should be exactly 8 lines long
- word_first_3 should contain the first 3 letters of the variable word
- word_last_2 should contain the last 2 letters of the variable word
- middle_word should contain the value of the variable word without the first and last letters
```
0$ ./7-edges.py
First 3 letters: Hol
Last 2 letters: on
Middle word: olberto
```
8. Create a new sentence
Complete this [source code](https://github.com/alx-tools/0x00.py/blob/master/8-concat_edges.py) to print object-oriented programming with Python, followed by a new line.

- You can find the source code here
- You are not allowed to use any loops or conditional statements
- Your program should be exactly 5 lines long
- You are not allowed to create new variables
- You are not allowed to use string literals

9. Easter Egg
Write a Python script that prints “The Zen of Python”, by TimPeters, followed by a new line.

Your script should be maximum 98 characters long (please check with wc -m 9-easter_egg.py)
```bash
@ubuntu:~/py/0x00$ ./9-easter_egg.py
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!

```
## Authors

[@selemandaffy](https://www.github.com/daffix)

![GitHub followers](https://img.shields.io/github/followers/DaffiX)

![YouTube Channel Subscribers](https://img.shields.io/youtube/channel/subscribers/UC0TUPSakz3GnB4nmbN0RXKw)
## License
Disclaimer:

The materials and questions provided in this repository are the property of ALX Africa and are intended solely for educational purposes as part of the ALX Software Engineering Program. These materials are designed to support the learning journey of students enrolled in the ALX SE Program and should not be reproduced, distributed, or shared without proper authorization from ALX Africa.

Please note that the content provided in this repository may be subject to change, and it is the responsibility of the ALX SE Program students to ensure they are using the most up-to-date materials provided by ALX Africa.

For more information about the ALX Africa programs, please visit their official website at [ALX Africa](https://www.alxafrica.com/)


