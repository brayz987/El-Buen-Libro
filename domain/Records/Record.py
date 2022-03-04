from datetime import datetime

class Record:
    __datetimeatr:str
    __type:str
    __item:str
    _totalprice:str


    def __init__(self, item:str, type:str) -> None:
        self.__datetimeatr = datetime.now()
        self.__type = type
        self.__item = item
        self._totalprice = 0

    def auditLog(self) -> None:
        print('It was started the audit for that record')
    
    def checkDiscount(self) -> None:
        print('It was verified the discount')

    def pay(self) -> None:
        print('It proced to pay the record')

    def checkItem(item:str) -> None:
        print('The item was checked')
    
    def verifyClient(client:str) -> None:
        print('Se realizo la confirmacion de datos del cliente')
    
    def alarm(self) -> None:
        print('It was informed to the employees about the backwardness')

    def getData(self) -> None:
        print(f'''
        The record count with the next information:
        Date and Time: {self.__datetimeatr}
        Type: {self.__type}
        Item: {self.__item}
        Price: {self._totalprice}
        ''')
