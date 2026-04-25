from typing import override

from oopConcepts.formulamethods import FormulaMethods


class Rectangle(FormulaMethods):
    def __init__(self, l, b):
        self.len = l
        self.brea = b

    @override
    def calculate_area(self):
        return self.len * self.brea

    @override
    def calculate_perimeter(self):
        return 2 * (self.brea + self.len)