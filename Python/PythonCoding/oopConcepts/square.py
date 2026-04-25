from typing import override

from oopConcepts.formulamethods import FormulaMethods


class Square(FormulaMethods):
    def __init__(self, s):
        self.side = s

    @override
    def calculate_area(self):
        return self.side * self.side

    @override
    def calculate_perimeter(self):
        return 4 * self.side