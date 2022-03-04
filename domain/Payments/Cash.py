from domain.Payments.PaymentMethod import PaymentMethod

class Cash(PaymentMethod):
    __valuereceived:int

    def __init__(self, client:str, valuereceived:int) -> None:
        PaymentMethod.__init__(self, client, type="Cash")
        self.__valuereceived = valuereceived

    def calculateLaps(self):
        print('The laps was...')
