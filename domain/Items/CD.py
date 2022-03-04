from domain.Items.Item import Item

class CD(Item):

    __artist:str
    __gender:str
    __tracks:str

    def __init__(self ,name:str, yearpublication:int, condition:str, saleprice:int, rentalprice:int , invunits:int, artist:str, gender:str, tracks:str) -> None:
        Item.__init__(self, name, yearpublication, condition, saleprice, rentalprice, invunits, type='CD')
        self.__artist = artist
        self.__gender = gender
        self.__tracks = tracks

    def delete(self) -> None:
        print ("The item was deleted successfully")
    
    def lend(self) -> None:
        print('The item was lend')

    def sell(self) -> None:
        print('The item was sell')
    
    def toUpdate(self) -> None:
        print('The item was updated')
    
    def create(name:str, yearpublication:int, condition:str, saleprice:int, rentalprice:int , invunits:int, artist:str, gender:str, tracks:str):
        print("The item was created")