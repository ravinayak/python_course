class Shapes:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
class Rectangle(Shapes):
    def __init__(self, width, height):
        super().__init__(width, height)
        
    @property
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return (2 * self.width) + (2 * self.height)
    
class Square(Shapes):
    def __init__(self, width, height):
        super().__init__(width, height)
        
    def area(self):
        return self.width * self.height
    
    @property
    def perimeter(self):
        return (4 * self.width)
    

     