1. pip   is the name of the command line tool commonly used to install, update, and remove external Python modules
2. info about function :https://docs.python.org/3/library/functions.html#open 

3. ``#!/usr/bin/env`` python3 uses the operating system env command, which locates and executes Python by searching the PATH environment variable. Unlike Windows, the Python interpreter is usually already in the $PATH variable on linux, so you don't have to add it.
4. ``sudo chmod +x health_checks.py`` Fix permission denied error. 
    This is because the above command tries to run your script directly as a program. The program is parsed by the interpreter specified in the first line of the script, i.e. shebang. If the kernel finds that the first two bytes are #! it uses the rest of the line as an interpreter and passes the file as an           argument. So, to do this, the file needs to have execute permission
5. **Access to VM**
- chmod 600 ~/Downloads/qwiklabs-L6868193.pem
-  ssh -i ~/Downloads/qwikLABS-XXXXX.pem username@External Ip Address : ``ssh -i ~/Downloads/qwiklabs-L6590716.pem student-01-6bba6a24b212@34.123.203.47``
- **execute** : ``./health_checks.py``
- **nano editor to open the file : ** ``./health_checks.py``
- **import module :** ``sudo apt install python3-requests``
- **Import the request module into the file using the import statements. :** ``import requests``
- **import network module (python file created ) : ** ``from network import *``

sudo chmod 777 script.py




Shout out to [regex101.com](https://www.coursera.org/learn/python-operating-system/supplement/NVXqf/regular-expressions-cheat-sheet#:~:text=Module%20Review-,Regular%20Expressions%20Cheat%2DSheet,regex101.com%2C%20which%20will%20explain%20each%20stage%20of%20a%20regex.,-Mark%20as%20completed), which will explain each stage of a regex. 
### Advanced Regular Expressions Cheat-Sheet
https://regexcrossword.com/

## More About Input Functions
Python 2 and Python 3 handle input and raw_input differently.

In Python 2

- input(x) is roughly the same as eval(raw_input(x))

- raw_input() is preferred, unless the author wants to support evaluating string expressions.

- eval() is used to evaluate string expressions.

Standard Library Docs:

- https://docs.python.org/2/library/functions.html#input

- https://docs.python.org/2/library/functions.html#raw_input

- https://docs.python.org/2/library/functions.html#eval

In Python 3

- Input handles string as a generic string. It does not evaluate the string as a string expression.

- raw_input doesn’t exist, but with some tricky techniques, it can be supported.

- eval() can be used the same as Python 2.

Standard Library Docs: 

- https://docs.python.org/3/library/functions.html#input

- https://docs.python.org/3/library/functions.html#eval

## Python Subprocesses Cheat Sheet
Check out the following link for more information:

https://docs.python.org/3/library/subprocess.html


import unittest

class TestCompiler(unittest.TestCase):

    def test_basic(self):
        testcase = "The best preparation for tomorrow is doing your best today."
        expected = ['b', 'a', 'a', 'b', 'a']
        self.assertEqual(LetterCompiler(testcase), expected)
unittest.main()

Yikes! SystemExit: True means an error occurred, as expected. The reason is that unittest.main( ) looks at sys.argv. In Jupyter, by default, the first parameter of sys.argv is what started the Jupyter kernel which is not the case when executing it from the command line. This default parameter is passed into unittest.main( ) as an attribute when you don't explicitly pass it attributes and is therefore what causes the error about the kernel connection file not being a valid attribute. Passing an explicit list to unittest.main( ) prevents it from looking at sys.argv.

Let's pass it the list ['first-arg-is-ignored'] for example. In addition, we will pass it the parameter exit = False to prevent unittest.main( ) from shutting down the kernel process. Run the following cell with the argv and exit parameters passed into unittest.main( ) to rerun your automatic test.

``unittest.main(argv = ['first-arg-is-ignored'], exit = False)``



