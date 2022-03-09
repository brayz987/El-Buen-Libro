from time import process_time_ns
from .DataBase import DataBase
import mysql.connector

class Mysql(DataBase):
    
    __mydb=None
    __mycursor=None
    __myconeccion:object
    

    def __init__(self, host:str, database:str, password:str, port:str, user:str):
        DataBase.__init__(self, host, database, password, port, user) #solo se puede llamr al constructor de la clase padre con DATABASE, los atributos y métodos se hacen con self

    
    def connect(self)-> bool:
        try:
            self.__mydb = mysql.connector.connect(

                host=self._host,
                user=self._user,
                password=self._password,
                database= self._database
            )
            self.__mycursor=self.__mydb.cursor()
            print("Database connected")
            return True

        except Exception as err:
            print(err)
            return False
    
    # def createconnection():
    #     Mysql.myconeccion=Mysql("127.0.0.1","elbuenlector","Brayan711737","3306","root")
    #     Mysql.myconeccion.connect()
    #     return Mysql.myconeccion

# Method permit insert a user to DB

    def insertDBUser(self,data,role:str)->bool:
        role = role.capitalize()
        # Mysql.createconnection()
        try:
            sql = f"INSERT INTO users (name, lastname, age, typeidentification, identification, phone, role) VALUES (%s, %s, %s, %s, %s, %s, %s)"            
            val = (data["name"],data["lastname"],data["age"],data["typeidentification"],data["identification"], data["phone"] , role)
            self.__mycursor.execute(sql, val)
            self.__mydb.commit()
            print("Dato insertado")
            return True
        except Exception as err:
            print(err)
            return False


# Method permit insert a item to DB, valid the last id of the table item
    def insertDBitem(self, data,type)->bool:
        self.__mycursor.execute("SELECT MAX( id ) FROM `item`")
        id = self.__mycursor.fetchone()
        
        if(id[0]==None):
            iditem = 0
        else:
            iditem = id[0]+1

        try:
            sql = f"INSERT INTO item (`id`,`name`, `type`, `condition`, `saleprice`, `rentalprice`, `invunits`) VALUES (%s, %s, %s, %s, %s, %s, %s)"            
            val = (iditem, data["name"],type,data["condition"],data["saleprice"],data["rentalprice"], data["invunits"])
            self.__mycursor.execute(sql, val)
            self.__mydb.commit()
            print("1 record inserted in table item with ID:", iditem)
            print("Dato insertado")
        except Exception as err:
            print(err)

# In case de item was type CD the program also insert the data in the table CD, valid de last id from table CD and add the item id to foreing Key

        if(type=="cd"): 
            self.__mycursor.execute("SELECT MAX( id ) FROM `cd`")
            id = self.__mycursor.fetchone()
        
            if(id[0]==None):
                idcd = 0
            else:
                idcd = id[0]+1

            try:
                sql = f"INSERT INTO cd (`id`,`artist`, `gender`, `tracks`,`iditem`) VALUES (%s, %s, %s, %s, %s)"            
                val = (idcd, data["artist"],data["gender"],data["tracks"],iditem)
                self.__mycursor.execute(sql, val)
                self.__mydb.commit()
                print("1 record inserted in table CD with ID:", idcd, "and Foreing Key ID:", iditem)
                print("Dato insertado")
            except Exception as err:
                print(err)

# In case de item was type Movie the program also insert the data in the table movie, valid de last id from table movie and add the item id to foreing Key

        if(type=="movie"): 
            self.__mycursor.execute("SELECT MAX( id ) FROM `movie`")
            id = self.__mycursor.fetchone()
        
            if(id[0]==None):
                idmovie = 0
            else:
                idmovie = id[0]+1

            try:
                sql = f"INSERT INTO movie (`id`,`producer`, `gender`, `classification`,`iditem`) VALUES (%s, %s, %s, %s, %s)"            
                val = (idmovie, data["producer"],data["gender"],data["classification"],iditem)
                self.__mycursor.execute(sql, val)
                self.__mydb.commit()
                print("1 record inserted in table movie with ID:", idmovie, "and Foreing Key ID:", iditem)
                print("Dato insertado")
            except Exception as err:
                print(err)

# In case de item was type Book the program also insert the data in the table book, valid de last id from table book and add the item id to foreing Key

    
        if(type=="book"): 
            self.__mycursor.execute("SELECT MAX( id ) FROM `book`")
            id = self.__mycursor.fetchone()
        
            if(id[0]==None):
                idbook = 0
            else:
                idbook = id[0]+1

            try:
                sql = f"INSERT INTO book (`id`,`writer`, `gender`, `editorial`,`iditem`) VALUES (%s, %s, %s, %s, %s)"            
                val = (idbook, data["writer"],data["gender"],data["editorial"],iditem)
                self.__mycursor.execute(sql, val)
                self.__mydb.commit()
                print("1 record inserted in table movie with ID:", idbook, "and Foreing Key ID:", iditem)
                print("Dato insertado")
            except Exception as err:
                print(err)


# In case de item was type Video the program also insert the data in the table video and item, valid de last id from table video and add the item id to foreing Key

    
        if(type=="video"): 
            self.__mycursor.execute("SELECT MAX( id ) FROM `video`")
            id = self.__mycursor.fetchone()
        
            if(id[0]==None):
                idvideo = 0
            else:
                idvideo = id[0]+1

            try:
                sql = f"INSERT INTO video (`id`,`creator`, `gender`,`iditem`) VALUES (%s, %s, %s, %s)"            
                val = (idvideo, data["creator"],data["gender"],iditem)
                self.__mycursor.execute(sql, val)
                self.__mydb.commit()
                print("1 record inserted in table video with ID:", idvideo, "and Foreing Key ID:", iditem)
                print("Dato insertado")
            except Exception as err:
                print(err)


# This method permit insert the client's payments in de DB

    def insertDBPayment(self, data,type)->bool:
        if(type == "cash"):
            self.__mycursor.execute("SELECT MAX( id ) FROM `cash`")
            id = self.__mycursor.fetchone()
        
            if(id[0]==None):
                idcash = 0
            else:
                idcash = id[0]+1


            try:
                sql = f"INSERT INTO cash (`id`,`identification`,`value`) VALUES (%s, %s, %s)"            
                val = (idcash, data["identification"], data["value"])
                self.__mycursor.execute(sql, val)
                self.__mydb.commit()
                print("1 record inserted in table cash with ID:", idcash)
                print("Dato insertado")
            except Exception as err:
                print(err)

        if(type == "creditcard"):
            self.__mycursor.execute("SELECT MAX( id ) FROM `creditcard`")
            id = self.__mycursor.fetchone()
        
            if(id[0]==None):
                idcreditcard = 0
            else:
                idcreditcard = id[0]+1


            try:
                sql = f"INSERT INTO creditcard (`id`,`identification`,`expirationdate`,`digits`,`quotas`) VALUES (%s, %s, %s, %s, %s)"            
                val = (idcreditcard, data["identification"], data["expirationdate"], data["digits"], data["quotas"])
                self.__mycursor.execute(sql, val)
                self.__mydb.commit()
                print("1 record inserted in table cash with ID:", idcreditcard)
                print("Dato insertado")
            except Exception as err:
                print(err)