class Person:
    __name:str
    __lastname:str
    __age:int
    __typeidentification:str
    __identification:int
    __phone:int
    __role:str

    def __init__(self, name:str, lastname:str, age:int, typeidentification:str, identification:int,  phone:int, role:str) -> None:
        self.__name = name
        self.__lastname = lastname
        self.__age = age
        self.__typeidentification = typeidentification
        self.__identification = identification
        self.__phone = phone
        self.__role = role
    
    def getData(self):
        print(f'''
        The person count with the next information:
        Names: {self.__name}
        Lastnames: {self.__lastname}
        Age: {self.__age}
        Identification Type: {self.__typeidentification}
        Identification: {self.__identification}
        Phone: {self.__phone}
        Role: {self.__role}
        ''')


