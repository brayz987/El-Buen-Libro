from abc import ABC


class DataBase(ABC):

    _host:str
    _password:str
    _port:str
    _user:str
    _database:str


    def __init__(self, host:str,  database:str, password:str, port:str, user:str):
        self._host = host
        self._password = password
        self._port = port
        self._user = user
        self._database = database

    



