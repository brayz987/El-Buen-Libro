from domain.Records.Record import Record

class Devolution(Record):

    def __init__(self, item:str) -> None:
        Record.__init__(self, item, type="Devolution")

    def addUnit(self)-> None:
        print("One unit was add from the item's inventory")
    

    def checkBackLog(self)-> None:
        print("The previous record was checked")

    def calculateFine(self)-> None:
        print("Calculating fine")
        
    def create(self, item:str)-> None:
        print("The sale was created")
    