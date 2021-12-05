1. pip   is the name of the command line tool commonly used to install, update, and remove external Python modules
2. info about function :https://docs.python.org/3/library/functions.html#open 
## Files and Directories Cheat-Sheet
- https://docs.python.org/3/library/os.html
- https://docs.python.org/3/library/os.path.html
- https://en.wikipedia.org/wiki/Unix_time
## CSV Files Cheat Sheet
- https://docs.python.org/3/library/csv.html
- https://realpython.com/python-csv/

## Regular Expressions Cheat-Sheet
Check out the following links for more information:

- https://docs.python.org/3/howto/regex.html
- https://docs.python.org/3/library/re.html
- https://docs.python.org/3/howto/regex.html#greedy-versus-non-greedy

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



