from src.calculations import Calculations


class TestCalc:
    calc = Calculations()

    def test_area_of_sqr(self):
        res = self.calc.area_of_sqr(10)
        assert res == 100, 'Area is wrong'

    def test_area_of_rectangle(self):
        res = self.calc.area_of_rectangle(10, 5)
        assert res == 50, 'Area is wrong'