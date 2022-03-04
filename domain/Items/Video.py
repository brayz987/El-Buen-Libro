from domain.Items.Item import Item

class Video(Item):

    __creator:str
    __gender:str

    def __init__(self ,name:str, yearpublication:int, condition:str, saleprice:int, rentalprice:int , invunits:int, creator:str, gender:str) -> None:
        Item.__init__(self, name, yearpublication, condition, saleprice, rentalprice, invunits, type='Video')
        self.__creator = creator
        self.__gender = gender

    def delete(self) -> None:
        print ("The item was deleted successfully")
    
    def lend(self) -> None:
        print('The item was lend')

    def sell(self) -> None:
        print('The item was sell')
    
    def toUpdate(self) -> None:
        print('The item was updated')
    
    def create(name:str, yearpublication:int, condition:str, saleprice:int, rentalprice:int , invunits:int, creator:str, gender:str):
        print("The item was created")