import pytest
from labwithtests.lib import fib as f


#Тест функции, возвращающей список из n первых чисел Фибоначчи
class TestFib:
    #Тест функции на корректных данных (n > 0)
    def test_on_correct_n(self):
        assert f.fib(5) == [1, 1, 2, 3, 5]
    #Тест функции на граничных данных (n == 0)
    def test_on_border_n(self):
        assert f.fib(0) == []
    #Тест функции на не корректных данных (n < 0), функция вызывает ValueError
    def test_on_incorrect_n(self):
        with pytest.raises(ValueError):
            f.fib(-10)

