from domain.Items.Item import Item

class Movie(Item):

    __producer:str
    __gender:str
    __classification:str

    def __init__(self ,name:str, yearpublication:int, condition:str, saleprice:int, rentalprice:int , invunits:int, producer:str, gender:str, classification:str) -> None:
        Item.__init__(self, name, yearpublication, condition, saleprice, rentalprice, invunits, type='Movie')
        self.__gender = gender
        self.__producer = producer
        self.__classification = classification

    def delete(self) -> None:
        print ("The item was deleted successfully")
    
    def lend(self) -> None:
        print('The item was lend')

    def sell(self) -> None:
        print('The item was sell')
    
    def toUpdate(self) -> None:
        print('The item was updated')
    
    def create(name:str, yearpublication:int, condition:str, saleprice:int, rentalprice:int , invunits:int, producer:str, gender:str, classification):
        print("The item was created")