import pytest
from tests.maths_operations import divide, subtract, add, multiply

def test_divide_by_zero_error():
    y = 0
    x = 2
    # This syntax is used to capture a block in which to test for a specific context
    # Here we are testing for a ValueError being raised as we perform a division by 0
    # exc_info: Think of it as a special container that pytest gives you. When the
    # code inside the with block successfully raises the expected ValueError, pytest
    # "catches" that error and puts all of its details into the exc_info container
    # for you to inspect.

	# What's Inside exc_info?
	# The ExceptionInfo object has a few very useful attributes:

	# 1. exc_info.value: This is the most common one you'll use. It holds the actual
 	# exception instance that was raised. By calling str(exc_info.value), you get the
  	# error message string, which is exactly what your test does to verify the message
   	# is correct.
   
	# 2. exc_info.type: This holds the type of the exception (e.g., <class 'ValueError'>)
 
	# 3. exc_info.traceback: This gives you the full traceback object, which is useful
 	# for more advanced debugging or logging scenarios.
  
	# Summary: In short, exc_info is your tool for looking inside the exception to make
 	# sure it's not just the right type of error, but that it also has the right message
  	# or other properties.
   
    with pytest.raises(ValueError) as exc_info:
        divide(x, y)
    # The assertion should be outside the 'with' block to check the captured exception.
    assert str(exc_info.value) == 'Division by 0 is not allowed'

# To capture any output use capsys. Pass capsys as an argument to the method in which 
# we want to test for print statement execution.
# capsys.readouterr() gives us captured object
# captured.out contains the print statement's input
# Always append \n at the end of the statement being asserted for equality, this is because print
# appends \n at the end of the statement

def test_divide(capsys):
    y = 2
    x = 4
    assert divide(x, y) == 2
    
    captured = capsys.readouterr()
    assert captured.out == 'Result of division of x by y is 2.00\n'
    
def test_add():
    x = 3
    y = 2
    assert add(x, y) == 5
    
def test_multiply():
    x = 3.75
    y = 4.25
    # Preferred Syntax
    assert multiply(x, y) == 15.94
    
def test_subtract(capsys):
    x = 4
    y = 2
    assert subtract(x, y) == 2
    
    captured = capsys.readouterr()
    assert(captured.out) == 'Result of x - y is 2.00\n'
    