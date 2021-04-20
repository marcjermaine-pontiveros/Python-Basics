class Point():
    # A method defining how to create a point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # ways to represent the objects as string    
    def __str__(self):
        return f"({self.x}, {self.y})"

    # ways to represent the objects as string    
    def __repr__(self):
        return f"({self.x}, {self.y})"
