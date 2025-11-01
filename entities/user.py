from datetime import datetime


class User:

    def __init__(self, firstname:str, lastname:str, email:str, password:str, create_at:str, update_at:str):
        self.__firstname = firstname
        self.__lastname = lastname
        self.__email = email
        self.__password = password
        self.__creat_at = create_at
        self.__update_at = update_at


    @classmethod
    def create(cls,firstname:str, lastname:str, email:str, password:str):
        return User(
            firstname=firstname,
            lastname=lastname,
            email=email,
            password=password,
            create_at=datetime.now(),
            update_at=None )

    def update(self, firstname:str = None, lastname:str = None):
        if firstname is not None:
            self.__firstname = firstname
        if lastname is not None:
            self.__lastname = lastname

    
    def __repr__(self):
        return f"(firstname: {self.__firstname}, lastname: {self.__lastname}, email: {self.__email}, password: {self.__password}, create_at:{self.__creat_at}, update_at:{self.__update_at})"