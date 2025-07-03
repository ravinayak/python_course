import pytest
from playlists.shapes import Rectangle, Square

# To print statements from test methods, use "-s" option
# pytest tests/test_shapes.py -s

# Here’s a step-by-step breakdown of what happens when you run
# pytest on your test_shapes.py file:

# 1. Test Discovery
# First, pytest scans your project for things that look like tests.
# By default, it looks for:

# Files named test_*.py or *_test.py. Your file tests/test_shapes.py
# matches this.
# Inside those files, it looks for classes prefixed with Test
# (like your TestRectangle and TestSquare) and functions prefixed
# with test_.
# 2. Class Instantiation and Test Execution
# This is the key part of your question. When pytest finds a class
# like TestRectangle, it does not just create one single object for
# the whole class. Instead, to ensure tests are completely isolated
# from each other, it follows this lifecycle for each test method inside
# the class:

# Create a New Instance: pytest creates a fresh instance of the TestRectangle
# class.
# Run Setup (if present): It looks for special setup methods. It sees
# setup_method and runs it on the new instance. This is where self.my_rectangle
# gets created in your first two tests.
# Run the Test Method: It calls the actual test method (e.g., test_area())
# on that instance.
# Run Teardown (if present): After the test method finishes
# (whether it passes, fails, or errors), pytest calls the teardown_method for
# cleanup.
# This entire cycle repeats for test_perimeter(), test_area_using_fixture(),
# and every other test method in the class. This guarantees that the state
# from one test (e.g., if you were to change self.my_rectangle.width) cannot
# accidentally affect the next test.

# 3. The Role of Fixtures
# For your tests like test_area_using_fixture(self, my_rectangle), pytest
# does something slightly different but with the same goal:

# When pytest sees that a test method requests an argument (my_rectangle)
# that matches the name of a function decorated with @pytest.fixture, it
# runs that fixture function first.
# The value returned by the fixture (return Rectangle(30, 50)) is then
# passed directly into the test method as an argument.
# Fixtures are the more modern and powerful way to handle setup in pytest.
# They make dependencies explicit and are more flexible than
# setup_method/teardown_method.

class TestRectangle:
	# Any method defined inside a class, including a pytest fixture, must accept self as its first parameter.
 
	# Setup/Teardown methods are called before execution of each method in the test class
	# How Pytest finds tests to run
	# Pytest uses auto discovery to find tests:
	# 	a. It looks at files which have test_ appended to them
	# 	b. It looks at methods in the files which have test_appended to them
	# 	c. It looks at methods signatures, if they have decorators and applies to tests and executes them
    def setup_method(self, method):
        self.my_rectangle = Rectangle(30, 50)
        print(f'method {method} is calling setup')
        
    def teardown_method(self, method):
        print(f'method {method} is calling teardown')
    
    # Here we define a fixture using pytest convention
    @pytest.fixture
    def my_rectangle(self):
        return Rectangle(30, 50)

    def test_area(self):
        assert self.my_rectangle.area == 1500
        
    def test_perimeter(self):
        assert self.my_rectangle.perimeter() == 160
    
    # pytest automatically deduces that my_rectangle provided in the method signature
    # as a 2nd argument is a fixture and generates the fixture before calling this method
    # think of fixture as a factory which generates objects on the fly before each method
    # which consumes the fixture as an argument can use it
    def test_area_using_fixture(self, my_rectangle):
        assert my_rectangle.area == 1500
        
    def test_perimeter_using_fixture(self, my_rectangle):
        assert my_rectangle.perimeter() == 160
        

class TestSquare:
    def setup_method(self, method):
        print(f'Setup method called from {method}')
        self.my_square = Square(30, 30)
    
    def teardown_method(self, method):
        print(f'Teardown method called from {method}')
        
    @pytest.fixture
    def my_square(self):
        return Square(30, 30)
    
    def test_area(self):
        assert self.my_square.area() == 900
    
    def test_perimeter(self):
        assert self.my_square.perimeter == 120
        
    def test_area_using_fixture(self, my_square):
        assert my_square.area() == 900
        
    def test_perimeter_using_fixture(self, my_square):
        assert my_square.perimeter == 120