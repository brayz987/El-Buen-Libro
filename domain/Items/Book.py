from domain.Items.Item import Item

class Book(Item):

    __writer:str
    __gender:str
    __editorial:str

    def __init__(self ,name:str, yearpublication:int, condition:str, saleprice:int, rentalprice:int , invunits:int, writer:str, gender:str, editorial:str) -> None:
        Item.__init__(self, name, yearpublication, condition, saleprice, rentalprice, invunits, type='Book')
        self.__writer = writer
        self.__gender = gender
        self.__editorial = editorial

    def delete(self) -> None:
        print ("The item was deleted successfully")
    
    def lend(self) -> None:
        print('The item was lend')

    def sell(self) -> None:
        print('The item was sell')
    
    def toUpdate(self) -> None:
        print('The item was updated')
    
    def create(name:str, yearpublication:int, condition:str, saleprice:int, rentalprice:int , invunits:int, writer:str, gender:str, editorial:str):
        print("The item was created")