from domain.Payments.PaymentMethod import PaymentMethod

class Cash(PaymentMethod):
    __valuereceived:int

    def __init__(self, clientIdentification:str, valuereceived:int) -> None:
        PaymentMethod.__init__(self, clientIdentification, type="Cash")
        self.__valuereceived = valuereceived

    def calculateLaps(self):
        print('The laps was...')
