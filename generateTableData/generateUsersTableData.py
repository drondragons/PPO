from re import sub
from faker import Faker
from dataclasses import dataclass
from string import ascii_letters, digits
from random import randint, choice, getrandbits

from AttributeValidator import Validator
from HandlerCSV import CSVHandler_dataclass
from generateRolesTableData import RolesGenerator


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


    def is_newLogin(self, login, users):
        is_new = True
        
        for user in users:
            if login == user.login:
                is_new = False
                break

        return is_new


    def generateUserLogin(self, fake):
        login = fake.user_name()
        while not 8 <= len(login) <= 50:
            login = fake.user_name()
        return login


    def generateUserEmail(self, fake, login):
        return f"{login}@{fake.free_email_domain()}"


    def choiceRole(self, roles_amount):
        roles = list()
        for key, value in roles_amount.items():
            if value:
                roles.append(key)

        return roles


    def generateUserRoleId(self, roles_dict):
        handler = CSVHandler_dataclass(RolesGenerator.file_path,
                                       RolesGenerator.class_type)
        roles = handler.getCSVData()

        role_id = 1
        role_name = choice(self.choiceRole(roles_dict))
        for i, role in enumerate(roles, 1):
            if role.name == role_name:
                role_id = i
                roles_dict[role_name] -= 1
                break

        return role_id


    def generateUserInitials(self, fake, person_sex=['male', 'female']):
        sex = choice(person_sex)
        
        last_name = getattr(fake, f"last_name_{sex}")()
        first_name = getattr(fake, f"first_name_{sex}")()
        middle_name = getattr(fake, f"middle_name_{sex}")()

        return f"{last_name} {first_name} {middle_name}"


    def generateUserPassword(self):
        password = str()
        symbols_amount = randint(8, 10)
        possible_symbols = f"{ascii_letters}{digits}-_~"
        
        for _ in range(symbols_amount):
            password += choice(possible_symbols)
            
        return password
    

    def generateUserActuality(self):
        return bool(getrandbits(1))


    def generateUserPhoneNumber(self, fake):
        phone = sub('[ \(\)\-]', '', fake.phone_number())
        return sub('(\+7)', '8', phone)


    def generateUserBirthDate(self, fake):
        return fake.date_of_birth(None, 5, 70).strftime("%d.%m.%Y")

        
    def generateUser(self, fake, login, roles_dict):
        return User(login=login,
                    email=self.generateUserEmail(fake, login),
                    initials=self.generateUserInitials(fake),
                    role_id=self.generateUserRoleId(roles_dict),
                    phone_number=self.generateUserPhoneNumber(fake),
                    password=self.generateUserPassword(),
                    birth_date=self.generateUserBirthDate(fake),
                    actuality=self.generateUserActuality())
    

    def generateUsers(self, locale="ru_RU", limit=1000):
        users = list()
        roles_dict = dict({'читатель': -1, 'библиотекарь': 5,
                           'администратор': 1})
                     
        fake = Faker(locale)
        while len(users) < limit:
            login = self.generateUserLogin(fake)
            if self.is_newLogin(login, users):
                users.append(self.generateUser(fake, login, roles_dict))
            
        return users


    def generate(self):
        self.container = self.generateUsers()
