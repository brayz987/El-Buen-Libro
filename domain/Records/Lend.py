from domain.Records.Record import Record

class Lend(Record):

    __days:int

    def __init__(self, item:str, days:int) -> None:
        Record.__init__(self, item, type = "Lend")
        self.__days = days

    def checkRentalPrice(self)-> None:
        print("The item's price was verified")
    
    def subtractUnit(self)-> None:
        print("One unit is subtracted from the item's inventory")
    
    def create(self, item:str)-> None:
        print("The sale was created")
    
    def calculatePrice(self)-> None:
        print("The price was calculate")