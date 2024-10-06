from generator import create_random_login, create_random_password, create_random_firstname
from data_for_tests import RegistrationData
from urls import Urls
import allure
import requests
import pytest


class TestCreateCourier:

    @allure.title('Проверка на ошибку при создании дубликата курьера')
    @allure.description('Проверка кода и тела ответа.')
    def test_create_duplicate_courier(self):
        body = {
            'login': RegistrationData.login,
            'password': RegistrationData.password,
            'firstName': RegistrationData.firstname
        }
        response = requests.post(Urls.URL_create, json=body)
        assert response.status_code == 409 and response.json() == {'code': 409, 'message': 'Этот логин уже используется. Попробуйте другой.'}

    @allure.title('Проверка создания аккаунта')
    @allure.description('Проверка кода и тела ответа.')
    def test_create_random_courier_success(self):
        body = {
            'login': create_random_login(),
            'password': create_random_password(),
            'firstName': create_random_firstname()
        }
        response = requests.post(Urls.URL_create, json=body)
        assert response.status_code == 201 and response.json() == {'ok': True}

    @allure.title('Проверка на ошибку при создании курьера с повторным использованием логина')
    @allure.description('Проверка кода и тела ответа.')
    def test_create_courier_account_with_dublicated_login(self):
        body = {
            'login': RegistrationData.login,
            'password': create_random_password(),
            'firstName': create_random_firstname()
        }
        response = requests.post(Urls.URL_create, json=body)
        assert response.status_code == 409 and response.json() == {'code': 409, 'message': 'Этот логин уже используется. Попробуйте другой.'}

    @allure.title('Проверка на ошибку при создании курьера с незаполненными обязательными полями')
    @allure.description('Проверяются код и тело ответа.')
    @pytest.mark.parametrize('empty_creds', [
        {'login': create_random_login(), 'password': '', 'firstName': create_random_firstname()},
        {'login': '', 'password': create_random_password(), 'firstName': create_random_firstname()}
    ])
    def test_create_courier_account_with_empty_fields(self, empty_creds):
        response = requests.post(Urls.URL_create, json=empty_creds)
        assert response.status_code == 400 and response.json() == {'code': 400, 'message': 'Недостаточно данных для создания учетной записи'}
