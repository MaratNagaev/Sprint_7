from data_for_tests import OrderData
from urls import Urls
import pytest
import requests
import allure
import json


class TestCreateOrder:

    @allure.title('Проверка создания заказа с разными цветами')
    @allure.description('Исходя из требований, в системе можно указывать в заказе один цвет самоката, два цвета '
                        ' или не указывать вовсе.')
    @pytest.mark.parametrize('order_body', [
        OrderData.order_data_black, OrderData.order_data_grey,
        OrderData.order_data_two_colors, OrderData.order_data_no_colors
    ])
    def test_create_order_with_colors_success(self, order_body):
        order_body = json.dumps(order_body)
        headers = {'Content-Type': 'application/json'}
        response = requests.post(Urls.URL_create_order, data=order_body, headers=headers, timeout=10)
        assert response.status_code == 201 and 'track' in response.text
