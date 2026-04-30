import pytest

from src.calculations import Calculations


class TestCalculations:
    calc = Calculations()



    @pytest.mark.parametrize("n1, n2, exVal",[(5, 5, 10), (-5, -5, -10), (0, 5, 5)])

    def test_add(self, n1, n2, exVal):
        res = self.calc.add( n1, n2)
        assert res == exVal, 'Addition Error'


    @pytest.mark.parametrize("n1, n2, exVal", [(5, 5, 0), (-5, -5, -0), (0, 5, -5)])
    def test_sub(self, n1, n2, exVal):
        res = self.calc.sub( n1, n2)
        assert res == exVal, 'Subtraction Error'

    def test_mul(self):
        res = self.calc.mul( 10, 5)
        assert res == 50, 'Multiplication Error'

    def test_div(self):
        res = self.calc.div( 12, 6)
        assert res == 2, 'Division Error'

    @pytest.mark.skip(reason= 'not yet implemented')
    def test_ne(self):
        res = self.calc.ne( 6, 6)
        assert res == True, 'Not Equal'

    def test_diverr(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.div(10, 0)