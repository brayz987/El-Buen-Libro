from domain.Persons.Person import Person

class Admin(Person):

    def __init__(self, names:str, lastnames:str, age:int, typeidentification:str, identification:int,  phone:int, role:str = "Administrator") -> None:
        Person.__init__(self, names, lastnames, age, typeidentification, identification, phone, role)


    def toRegister(names:str, lastnames:str, age:int, typeidentification:str, identification:int,  phone:int)->bool:
        print(f'The Admin was registered')


    def generateReport(type:str)->bool:
        print(f'Generating')

    def createUser(names:str, lastnames:str, age:int, typeidentification:str, identification:int,  phone:int, role:str):
        print(f'The user was created')

        
    def deleteUser(user:str)->bool:
        print(f'The user was deleted')
    
    def modifyUser(user:str)->bool:
        print('The user was modify')
