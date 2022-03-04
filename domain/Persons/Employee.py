import imp
from domain.Persons.Person import Person
from domain.Persons.Client import Client


class Employee(Person):

    def __init__(self, names:str, lastnames:str, age:int, typeidentification:str, identification:int,  phone:int, role:str = "Employee") -> None:
        Person.__init__(self,names, lastnames, age, typeidentification, identification, phone, role)

    def toRegister(names:str, lastnames:str, age:int, typeidentification:str, identification:int,  phone:int)->bool:
        print(f'The Employee was registered')
    
    def queryItem(item:str)->object:       
        print('The item was query successfully')

    def queryClient(client:str)->object:        
        print('The client was query successfully')

    def registerNewItem()->bool:  
        print('The item was registered successfully')
    
    def registerSale():
        print('The sale was registered successfully')

    def registeerLoan()->bool:
        print('The loan was registered successfully')

    def registerRefund()->bool:   
        print('The refund was registered successfully')

    def registerClient(names:str, lastnames:str, age:int, typeidentification:str, identification:int,  phone:int):   
        Client.toRegister(names, lastnames, age, typeidentification, identification,  phone)
        print('The client was registered successfully')
