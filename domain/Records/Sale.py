from domain.Records.Record import Record

class Sale(Record):

    def __init__(self, item:str) -> None:
        Record.__init__(self, item, type = "Sale")

    def checkSalesPrice(self)-> None:
        print("The item's price was verified")
    
    def subtractUnit(self)-> None:
        print("One unit is subtracted from the item's inventory")
    
    def create(self, item:str)-> None:
        print("The sale was created")