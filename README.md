Тесты для API ручек сайта https://qa-scooter.praktikum-services.ru/

### Файлы репозитория

- allure_results.py содержит результаты тестов для составления отчета;
- директория tests содержит файлы с тестами
  test_create_courier.py - тест на создание курьера;
  test_login.py - тест на логин курьера;
  test_create_order.py - тест на создание заказа;
  test_orders_list.py - тест на получение списока заказов;
- data_for_tests.py содержит тестовые данные;
- generator.py генерирует логин, пароль и имя для тестов;
- pytest.ini файл конфигурации pytest;
- urls.py содерждит адрес сервиса и эндпоинтов;

### Запуск тестов

- pytest -v tests
