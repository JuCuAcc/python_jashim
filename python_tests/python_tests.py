
# A unit test verifies that one specific aspect of your code works as it's supposed to.
# A test case is a collection of unit tests which verify your code's behavior in a wide variety of situations.

# A passing test
# Python's unittest module provides tools for testing code.

# Building a testcase with one unit test
# To build a test case, make a class that inherits from
#   unittest.TestCase and write methods that begin with test_.


# Python provides a number of assert methods you can use to test your code.
# Verify that a == b or a != b

assertEqual(a,b)
assertNotEqual(a,b)

# Verify that x is True, or x is False
assertTrue(x)
assertFalse(x)

# Verify an item is in a list, or not in a list
assertIn(item, list)
assertNotIn(item, list)

# Testing a class
# Testing a class is similar to testing a function,
#   since you'll mostly be testing your methods.