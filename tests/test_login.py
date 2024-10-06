from generator import create_random_login, create_random_password
from data_for_tests import RegistrationData
from urls import Urls
import requests
import pytest
import allure


class TestLogin:

    @allure.title('Проверка на успешную аутентификацию курьера')
    @allure.description('Проверка кода и тела ответа.')
    def test_login_success(self):
        response = requests.post(Urls.URL_login, json=RegistrationData.valid_courier_data)
        assert response.status_code == 200 and 'id' in response.text

    @allure.title('Проверка на ошибку аутентификации курьера с невалидными данными')
    @allure.description('Проверяются код и тело ответа.')
    @pytest.mark.parametrize('wrong_creds', [
        {'login': create_random_login(), 'password': create_random_password()},
        RegistrationData.courier_data_with_wrong_password
    ])
    def test_login_with_wrong_creds(self, wrong_creds):
        response = requests.post(Urls.URL_login, json=wrong_creds)
        assert response.status_code == 404 and response.json() == {'code': 404, 'message': 'Учетная запись не найдена'}

    @allure.title('Проверка на ошибку аутентификации курьера с пустым полем логина или пароля')
    @allure.description('Проверяются код и тело ответа.')
    @pytest.mark.parametrize('empty_creds', [
        {'login': '', 'password': create_random_password()},
        {'login': RegistrationData.login, 'password': ''}
    ])
    def test_login_with_empty_fields(self, empty_creds):
        response = requests.post(Urls.URL_login, json=empty_creds)
        assert response.status_code == 400 and response.json() == {'code': 400, 'message': 'Недостаточно данных для входа'}
