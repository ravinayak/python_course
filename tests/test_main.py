import pytest
from main import divide, subtract, add, multiply

def test_divide_by_zero_error():
    y = 0
    x = 2
    with pytest.raises(ValueError) as exc_info:
        divide(x, y)
    # The assertion should be outside the 'with' block to check the captured exception.
    assert str(exc_info.value) == 'Division by 0 is not allowed'
    
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
    