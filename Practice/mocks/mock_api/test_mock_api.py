import json
import pytest
from unittest.mock import patch, MagicMock
from mock_api import get_weather, GOOD, BAD


class GettingWeatherTest:
    # Заменяем в пакете mock_api объект requests тестовым двойником.
    @patch('mock_api.requests')
    def test_good(self, requests_mock):
        # Подгружаем json-файл с реальным запросом и ответом на сервис
        with open('example_response.json', 'r') as f:
            # Присваиваем переменной json-response
            body = json.load(f)
        # Заменяем response mock-объектом
        request_response_mock = MagicMock()
        # Задаем атрибут status_code и значение, которое он имеет
        request_response_mock.status_code = 200
        # Задаем метод json и значение, которое он возвращает - пример реального API-Call'a
        request_response_mock.json.return_value = body
        # Теперь запрос будет возвращать mock-объект с заданным поведением
        requests_mock.get.return_value = request_response_mock
        # Проводим тест
        assert(get_weather('Dubai') == GOOD)

    @patch('mock_api.requests')
    def test_bad(self, requests_mock):
        request_response_mock = MagicMock()
        request_response_mock.status_code = 200
        request_response_mock.json.return_value = {'main': {'temp': 17}}
        requests_mock.get.return_value = request_response_mock

        assert(get_weather('Kharkov') == BAD)

    # Заменяем в пакете getting_weather объект requests тестовым двойником.
    @patch('mock_api.requests')
    def test_error_from_server(self, requests_mock):
        # Заменяем response mock-объектом
        request_response_mock = MagicMock()
        # Задаем атрибут status_code и значение, которое он имеет
        request_response_mock.status_code = 404
        # Задаем метод json и значение, которое он возвращает
        request_response_mock.json.return_value = {'message': "City not found"}
        # Теперь запрос будет возвращать mock-объект с заданным поведением
        requests_mock.get.return_value = request_response_mock
        # Проводим тест
        with pytest.raises(RuntimeError):
            get_weather('Kharkov')


if __name__ == '__main__':
    pytest.main()
