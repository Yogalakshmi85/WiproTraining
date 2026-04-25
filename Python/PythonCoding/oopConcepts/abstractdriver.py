from oopConcepts.rectangle import Rectangle
from oopConcepts.square import Square

sqobj = Square(10)

print(f'Area: {sqobj.calculate_area()}\tPerimeter: {sqobj.calculate_perimeter()}')

robj = Rectangle(10, 20)

print(f'Area: {robj.calculate_area()}\tPerimeter: {robj.calculate_perimeter()}')