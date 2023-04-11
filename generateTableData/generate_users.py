from re import sub
from faker import Faker
from dataclasses import dataclass
from string import ascii_letters, digits
from random import randint, choice, getrandbits

from validation import Validator
from generate_roles import RolesGenerator
from csv_handler import CSVHandler_dataclass


@dataclass(frozen=True)
class User:
    login: str = Validator(str, [Validator.exist_validator,
                                 Validator.symbols_validator,
                                 Validator.length_validator],
                           8, 50, "[^\~\-_a-zA-Z0-9]")
    email: str = Validator(str, [Validator.exist_validator,
                                 Validator.symbols_validator,
                                 Validator.length_validator],
                           8, 50, "[^\~\-\.\@_a-zA-Z0-9]")
    initials: str = Validator(str, [Validator.exist_validator,
                                    Validator.match_validator,
                                    Validator.length_validator],
                              1, 50, "^[а-яА-ЯёЁ\-]+ [а-яА-ЯёЁ\-]+ [а-яА-ЯёЁ\-]+$")
    role_id: int = Validator(int, [Validator.exist_validator])
    phone_number: str = Validator(str, [Validator.exist_validator,
                                        Validator.match_validator,
                                        Validator.length_validator],
                                  11, 11, "^8\d{10}$")
    password: str = Validator(str, [Validator.exist_validator,
                                    Validator.symbols_validator,
                                    Validator.length_validator],
                              8, 20, "[^\~\-_a-zA-Z0-9]")
    actuality: bool = Validator(bool, [])
    birth_date: str = Validator(str, [Validator.exist_validator,
                                      Validator.symbols_validator,
                                      Validator.length_validator],
                                5, 10, "[^\d\.]")


class UsersGenerator:
    class_type = User
    file_path = "../TableData/Users.csv"


    def __init__(self):
        self.container = list()


    def is_new_login(self, login, users):
        is_new = True
        
        for user in users:
            if login == user.login:
                is_new = False
                break

        return is_new


    def generate_login(self, fake):
        login = fake.user_name()
        while not 8 <= len(login) <= 50:
            login = fake.user_name()
        return login


    def generate_email(self, fake, login):
        return f"{login}@{fake.free_email_domain()}"


    def choice_role(self, roles_amount):
        roles = list()
        for key, value in roles_amount.items():
            if value:
                roles.append(key)

        return roles


    def generate_role_id(self, roles_dict):
        handler = CSVHandler_dataclass(RolesGenerator.file_path,
                                       RolesGenerator.class_type)
        roles = handler.get_csv_data()

        role_id = 1
        role_name = choice(self.choice_role(roles_dict))
        for i, role in enumerate(roles, 1):
            if role.name == role_name:
                role_id = i
                roles_dict[role_name] -= 1
                break

        return role_id


    def generate_initials(self, fake, person_sex=['male', 'female']):
        sex = choice(person_sex)
        
        last_name = getattr(fake, f"last_name_{sex}")()
        first_name = getattr(fake, f"first_name_{sex}")()
        middle_name = getattr(fake, f"middle_name_{sex}")()

        return f"{last_name} {first_name} {middle_name}"


    def generate_password(self):
        password = str()
        symbols_amount = randint(8, 10)
        possible_symbols = f"{ascii_letters}{digits}-_~"
        
        for _ in range(symbols_amount):
            password += choice(possible_symbols)
            
        return password
    

    def generate_actuality(self):
        return bool(getrandbits(1))


    def generate_phone_number(self, fake):
        phone = sub('[ \(\)\-]', '', fake.phone_number())
        return sub('(\+7)', '8', phone)


    def generate_birth_date(self, fake):
        return fake.date_of_birth(None, 5, 70).strftime("%d.%m.%Y")

        
    def generate_user(self, fake, login, roles_dict):
        return User(login=login,
                    email=self.generate_email(fake, login),
                    initials=self.generate_initials(fake),
                    role_id=self.generate_role_id(roles_dict),
                    phone_number=self.generate_phone_number(fake),
                    password=self.generate_password(),
                    birth_date=self.generate_birth_date(fake),
                    actuality=self.generate_actuality())
    

    def generate_users(self, locale="ru_RU", limit=1000):
        users = list()
        roles_dict = dict({'читатель': -1, 'библиотекарь': 5,
                           'администратор': 1})
                     
        fake = Faker(locale)
        while len(users) < limit:
            login = self.generate_login(fake)
            if self.is_new_login(login, users):
                users.append(self.generate_user(fake, login, roles_dict))
            
        return users


    def generate(self):
        self.container = self.generate_users()
