import pytest
from shapes import Rectangle, Square

# To print statements from test methods, use "-s" option
# pytest tests/test_shapes.py -s

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