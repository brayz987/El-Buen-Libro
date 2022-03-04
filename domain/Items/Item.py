class Item:
    __name:str
    __yearpublication:int
    __type:str
    __condition:str
    __saleprice:int
    __rentalprice:int
    __invunits:int
    __unitslend:int

    def __init__(self,name:str, yearpublication:int, condition:str, saleprice:int, rentalprice:int , invunits:int, type:str) -> None:
        self.__name = name
        self.__yearpublication = yearpublication
        self.__type = type
        self.__saleprice = saleprice
        self.__rentalprice = rentalprice
        self.__condition = condition
        self.__invunits = invunits
        self.__unitslend = 0
    
    def getData(self):
        print(f'''
        The item count with the next information:
        Name or Title: {self.__name}
        Year of publication: {self.__yearpublication}
        Type: {self.__type}
        Condition: {self.__condition}
        Sale Price: {self.__saleprice}
        Rental Price: {self.__rentalprice}
        Units in inventory: {self.__invunits}
        Units lend: {self.__unitslend}
        ''')