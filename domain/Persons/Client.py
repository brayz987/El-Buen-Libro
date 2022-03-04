from domain.Persons.Person import Person

class Client(Person):

    _affiliate:bool = False
    _timeaffiliate:int = 0
    _remainingaffiliation:int

    def __init__(self, names:str, lastnames:str, age:int, typeidentification:str, identification:int,  phone:int, role:str = "Client") -> None:
        Person.__init__(self, names, lastnames, age, typeidentification, identification, phone, role)

    def toRegister(names:str, lastnames:str, age:int, typeidentification:str, identification:int,  phone:int)->bool:
        print(f'The client was registered')

    def toDelete(self)->bool:
        print(f'The client {self._names} {self._lastnames} was deleted')


    def toUpdate(self)->bool:
        print(f'The client {self._names} {self._lastnames} was updated')


    def toAffiliate(self)->bool:
        print(f'The client {self._names} {self._lastnames} was affiliated')

    def renewAffiliate(self)->bool:
        print(f'The client {self._names} {self._lastnames} renewed his affiliation')