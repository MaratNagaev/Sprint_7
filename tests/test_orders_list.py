from urls import Urls
import allure
import requests


class TestGetOrdersList:

    @allure.title('Проверка на получение списка заказов')
    @allure.description('Проверка кода и тела ответа.')
    def test_get_orders_list_success(self):
        response = requests.get(Urls.URL_create_order)
        assert type(response.json()['orders']) == list and 'id' in response.json()['orders'][0]
