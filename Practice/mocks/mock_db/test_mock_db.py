# test_mock_db.py
import pytest
from unittest.mock import patch, MagicMock
from mock_db import search_db


class DatabaseSearchTest:
    # Указываем путь к модулю, который хотим пропатчить
    @patch('mock_db.create_engine')
    def test(self, create_engine_mock):
        # Заменяем con mock-объектом
        con_mock = MagicMock()
        # Задаем метод execute и значение, которое он возвращает
        con_mock.execute.return_value.fetchall.return_value = [(1, 'bizibaza-api', 2)]
        # В реальности возврат create_engine присваивается переменной eng,
        # Поэтому её тоже мочим.
        engine_mock = MagicMock()
        # Задаем метод connect и значение, которое он возвращает.
        # Не забываем про магический метод менеджера контекста.
        engine_mock.connect.return_value.__enter__.return_value = con_mock
        # Задаем метод create_engine и значение, которое он возвращает
        create_engine_mock.return_value = engine_mock
        # Помещаем результат поиска в res
        res = search_db('bizi')
        # Проводим тест
        assert(len(res) == 1)
        assert(res[0].name == 'bizibaza-api')


if __name__ == '__main__':
    pytest.main()
