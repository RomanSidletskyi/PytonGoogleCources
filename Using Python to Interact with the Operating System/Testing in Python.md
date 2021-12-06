## Unit Test Cheat-Sheet
Frankly, the unit testing library for Python is fairly well documented, but it can be a bit of a dry read. Instead, we suggest covering the core module concepts, and then reading in more detail later.

Best of Unit Testing Standard Library Module
Understand a Basic Example:

https://docs.python.org/3/library/unittest.html#basic-example

Understand how to run the tests using the Command Line:

https://docs.python.org/3/library/unittest.html#command-line-interface

Understand various Unit Test Design Patterns:

https://docs.python.org/3/library/unittest.html#organizing-test-code

Understand the uses of setUp, tearDown; setUpModule and tearDownModule

Understand basic assertions:
![image](https://user-images.githubusercontent.com/30626559/144759523-5c4308c9-a154-4426-bc32-9b9246574e16.png)



Understand more specific assertions such as assertRaises

- https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertRaises
## More About Tests
Check out the following links for more information:

- https://landing.google.com/sre/sre-book/chapters/monitoring-distributed-systems/

- https://landing.google.com/sre/sre-book/chapters/testing-reliability/

- https://testing.googleblog.com/2007/10/performance-testing.html

- https://www.guru99.com/smoke-testing.html

- https://www.guru99.com/exploratory-testing.html

№№ Handling Errors Cheat-Sheet
Raise allows you to throw an exception at any time.

- https://docs.python.org/3/tutorial/errors.html#raising-exceptions

Assert enables you to verify if a certain condition is met and throw an exception if it isn’t.

- https://docs.python.org/3/reference/simple_stmts.html#the-assert-statement

- https://stackoverflow.com/questions/5142418/what-is-the-use-of-assert-in-python

The standard library documentation is kind of unclear. Basically `assert <something false>` will raise AssertionError, which the caller may need to handle.

In the try clause, all statements are executed until an exception is encountered.

- https://docs.python.org/3/tutorial/errors.html#handling-exceptions

Except is used to catch and handle the exception(s) that are encountered in the try clause.

- https://docs.python.org/3/library/exceptions.html#bltin-exceptions

Other interesting Exception handling readings:

- https://doughellmann.com/blog/2009/06/19/python-exception-handling-techniques/

- https://testing.googleblog.com/2008/09/test-first-is-fun_08.html
