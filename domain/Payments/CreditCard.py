from domain.Payments.PaymentMethod import PaymentMethod

class CreditCard(PaymentMethod):
    __expirationdate:str
    __digits:int
    __bank:str
    __transactionnumber:int
    __quotas:int

    def __init__(self, identification:int, expirationdate:str, digits:int, quotas:int) -> None:
        PaymentMethod.__init__(self,identification,type="Credit Card")
        self.__expirationdate = expirationdate
        self.__digits = digits
        self.__quotas = quotas


    def verifyCard(self) -> None:
        print('The card was verified')
    
    def setQuotas(self, quotas:int) -> None:
        print('The quotas of the payment was set')
    
    def verifyPayment(self) -> None:
        print('The payment was verified with the bank')
