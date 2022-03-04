from domain.Payments.PaymentMethod import PaymentMethod

class DebitCard(PaymentMethod):
    __transaction:int

    def __init__(self, client:str) -> None:
        PaymentMethod.__init__(self, client, type = "DebitCard")

    def transaction(self):
        print('The transaction with the bank was started')
    
    def verifyPay(self):
        print('The pay was verified for the bank')
