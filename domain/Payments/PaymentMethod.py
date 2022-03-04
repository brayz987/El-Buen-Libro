class PaymentMethod:

    __type:str
    __client:str

    def __init__(self, client:str, type:str) -> None:
        self.__type = type
        self.__client = client

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
        Client: {self.__client}
        ''')
