from mypack.circle import areaOfCircle
from mypack.circle import perimeterOfCircle
from mypack.basicShapes import areaOfSquare
from mypack.basicShapes import areaOfRect
from mypack.basicShapes import perimeterOfSquare

radius = int(input('Enter radius '))

print('Area:', areaOfCircle(radius))
print('Perimeter:', perimeterOfCircle(radius))

area = int(input('Enter area '))

print('Area:', areaOfSquare(area))
print('Perimeter:', perimeterOfSquare(area))

len = int(input('Enter length '))
breadth = int(input('Enter breadth '))

print('Area: ', areaOfRect(len, breadth))