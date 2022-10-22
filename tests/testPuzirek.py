import pytest
from labwithtests.lib import puzirek as p


#Тест функции, реализующей сортировку пузырьком
class TestPuzirek:
    # Тест функции на корректных данных (arr - список)
    def test_on_correct_arr(self):
        assert p.puzirek([1,5,2,3,6,3,4]) == [1,2,3,3,4,5,6]
    # Тест функции на не корректных данных (arr - не список)
    def test_on_incorrect_arr(self):
        with pytest.raises(ValueError):
            p.puzirek(25)