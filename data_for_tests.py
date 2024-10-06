class RegistrationData:
    login = 'Marat1861'
    password = '12345q'
    firstname = 'Marat'
    valid_courier_data = {'login': 'Marat1861', 'password': '12345q', 'firstName': 'Marat'}
    courier_data_without_name = {'login': 'Marat1861', 'password': '12345q'}
    courier_data_with_wrong_password = {'login': 'Marat1861', 'password': '22321'}


class OrderData:
    order_data_grey = {
        'firstName': 'Валерчикс',
        'lastName': 'Тестовв',
        'address': 'Ленинскиий проспект, 12',
        'metroStation': 3,
        'phone': '+7 800 523 35 35',
        'rentTime': 2,
        'deliveryDate': '2024-09-28',
        'comment': 'туда-сюдаааа',
        'color': [
            'GREY'
        ]
    }

    order_data_black = {
        'firstName': 'Савелий',
        'lastName': 'Курганов',
        'address': 'Москоу, Варшавский проспект, 3',
        'metroStation': 3,
        'phone': '+7 925 432 77 88',
        'rentTime': 6,
        'deliveryDate': '2024-10-02',
        'comment': 'ох тесты мои тесты',
        'color': [
            'BLACK'
        ]
    }

    order_data_two_colors = {
        'firstName': 'Ольга',
        'lastName': 'Зайцева',
        'address': '300м от вас',
        'metroStation': 10,
        'phone': '+7 922 111 22 11',
        'rentTime': 5,
        'deliveryDate': '2024-10-03',
        'comment': 'Привет!',
        'color': [
            'BLACK', 'GREY'
        ]
    }

    order_data_no_colors = {
        'firstName': 'Валентин',
        'lastName': 'Киборг',
        'address': 'Авдеевка',
        'metroStation': 4,
        'phone': '+7 999 888 99 11',
        'rentTime': 2,
        'deliveryDate': '2024-10-04',
        'comment': 'написать комментарий',
        'color': []
    }