class PaymentMethod:

    __type:str
    __clientIdentification:int

    def __init__(self, clientIdentification:int, type:str) -> None:
        self.__type = type
        self.__clientIdentification = clientIdentification

    def create(self) -> None:
        print('The payment method  was created')
    
    def update(self) -> None:
        print('The payment method payment was update ')

    def delete(self) -> None:
        print('The payment method was deleted')


    def getData(self) -> None:
        print(f'''
        The Payment Method count with the next information:
        Type: {self.__type}
        Client: {self.__clientIdentification}
        ''')
