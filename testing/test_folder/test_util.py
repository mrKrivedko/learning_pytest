import pytest
# обратите внимание на импорт `util`
from util import str_to_int_list

@pytest.mark.parametrize("str_lst", [
    # определяем значения, которые будет 
    # принимать переменная `str_lst``
    ['8.3', '11', 'девять', '1', '5', '3'], 
    ['пять', '-1', '-13', '7', '3.9', '4'],
    ['5ять', '1,5', '6.3', '2,0', 'два', '9']
    ])
class Test_str_to_int_list():
    """Группа тестов, которая запускается с одними и теми же 
    параметрами и проверяет функцию на разные утверждения"""

    # переменная `str_lst` передается из  помощника
    # `@pytest.mark` в объект класса неявно
    def test_is_list(self, str_lst):
        """Результат должен быть в виде списка"""
        result = str_to_int_list(str_lst)
        assert isinstance(result, list)
                
    def test_int_to_list(self, str_lst):
        """Список должен содержать только целые числа"""
        result = str_to_int_list(str_lst)
        assert all([isinstance(n, int) for n in result])

    def test_0_10(self, str_lst):
        """Числа в списке должны быть в диапазоне от 0 до 10"""
        result = str_to_int_list(str_lst)
        assert all([0 <= n <= 10 for n in result])

# моделирование исключительных ситуаций
@pytest.mark.parametrize("str_lst", [
    # передается пустой список 
    [],
    # и список не содержащий цифры 
    ['1.ин', 'два', 'три', '4етыре']
    ])
def test_empty_list(str_lst):
    """Тест на исключительные ситуации"""
    result = str_to_int_list(str_lst)
    assert result == []