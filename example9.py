# Polimorfismo: Es una característica de la POO que se utiliza cuando se tienen métodos comunes nombrados en las clases o subclases y está realacionado con la herencia.

from turtle import circle


class Shape:
    def __init__(self): # inicializando los lados de la figuras
        self.sides = 0
    
    def getArea(self):
        pass

class Rectangle(Shape): # deriva de la clase shape
    def __init__(self, width = 0, heigth = 0):
        self.width = width
        self.heigth = heigth
        self.sides = 4
    
    def getArea(self):
        return (self.width * self.heigth)

class Circle(Shape): # deriva de la clase shape
    def __init__(self,radius = 0):
        self.radius = radius
    
    def getArea(self):
        return (3.1416 * self.radius * self.radius)


shapes = [Rectangle(5,10), Circle(6)]

print("Area of reactangle is : ", str(shapes[0].getArea()))
print("Area of circle is : ", str(shapes[1].getArea()))
