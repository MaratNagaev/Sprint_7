from faker import Faker

fake = Faker()
fake_rus = Faker(locale='ru_RU')

def create_random_firstname():
    first_name = fake_rus.first_name()
    return first_name

def create_random_login():
    login = fake.text(max_nb_chars=9) + str(fake.random_int(0, 999))
    return login

def create_random_password():
    password = fake.password(length=11, special_chars=True, digits=True, upper_case=True, lower_case=True)
    return password


