import pytest
from labwithtests.lib import calc as c


#Тест калькулятора
#Корректные данные для a и b - любые числа (int, float)
#Корректные данные для sign - '+', '-', '*', '/'
class TestCalc:
    #Тест сложения при корректных данных
    def test_plus_on_correct_a_and_b(self):
        assert c.calc(5, 4,'+') == 9
    #Тест сложения при не корректных данных
    def test_plus_on_incorrect_a_and_b(self):
        with pytest.raises(ValueError):
            c.calc(5, '4','+')
    #Тест вычитания при корректных данных
    def test_minus_on_correct_a_and_b(self):
        assert c.calc(5, 4,'-') == 1
    #Тест вычитания при не корректных данных
    def test_minus_on_incorrect_a_and_b(self):
        with pytest.raises(ValueError):
            c.calc(5, '4', '-')
    #Тест умножения при корректных данных
    def test_multiply_on_correct_a_and_b(self):
        assert c.calc(5, 4,'*') == 20
    #Тест умножения при не корректных данных
    def test_multiply_on_incorrect_a_and_b(self):
        with pytest.raises(ValueError):
            c.calc(5, '4','*')
    #Тест деления при корректных данных
    def test_divide_on_correct_a_and_b(self):
        assert c.calc(5, 4,'/') == 5/4
    #Тест деления при не корректных данных
    def test_divide_on_incorrect_a_and_b(self):
        with pytest.raises(ValueError):
            c.calc(5, '4', '/')
    #Тест не корректного знака
    def test_incorrect_sign_on_correct_a_and_b(self):
        with pytest.raises(ValueError):
            c.calc(5, 4, 'Б')
