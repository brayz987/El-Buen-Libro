import json
from flask import Flask, request
from database.Mysql import Mysql
from domain.Items.Book import Book
from domain.Items.Movie import Movie
from domain.Items.Video import Video
from domain.Payments.Cash import Cash
from domain.Payments.CreditCard import CreditCard
from domain.Payments.PaymentMethod import PaymentMethod
from domain.Persons.Admin import Admin
from domain.Persons.Person import Person
from domain.Persons.Client import Client
from domain.Persons.Employee import Employee
from domain.Items.CD import CD


app = Flask(__name__)


myconeccion=Mysql("127.0.0.1","elbuenlector","Brayan711737","3306","root")
myconeccion.connect()
print(myconeccion)

@app.route("/", methods=['GET'])
def hello():
    print(request.args.get("name"))
    print(request.args.get("lastname"))

    return {
        'title': 'Hello'
    }


# @app.route("/", methods=['POST'])
# def create_user():
#     data = json.loads(request.data)

#     person:Person=Person(data['name'],data['lastname'],data['age'],data['typeidentification'],data['identification'],data['phone'],data['role'])
#     print(person)
#     person.getData()

#     return {
#         "data": data,
#         "title": "Funciona!!!"
#     }

@app.route("/user/<role>", methods=["POST"])
def createUser(role:str):
    data = json.loads(request.data)

    if(role == "client"):
        person:Client=Client(data['name'],data['lastname'],data['age'],data['typeidentification'],data['identification'],data['phone'])
    elif(role == "employee"):
        person:Employee=Employee(data['name'],data['lastname'],data['age'],data['typeidentification'],data['identification'],data['phone'])
    elif(role == "admin"):
        person:Admin=Admin(data['name'],data['lastname'],data['age'],data['typeidentification'],data['identification'],data['phone'])

    person.getData()        
    myconeccion.insertDBUser(data,role)

    return {
        "title": "Dato insertado en la DB"
    }




@app.route("/item/<type>", methods=["POST"])
def createItem(type):
    data = json.loads(request.data)
    if(type=="cd"):
        item:CD=CD(data["name"],data["yearpublication"],data["condition"],data["saleprice"],data["rentalprice"],data["invunits"],data["artist"],data["gender"],data["tracks"])
    if(type=="movie"):
        item:Movie=Movie(data["name"],data["yearpublication"],data["condition"],data["saleprice"],data["rentalprice"],data["invunits"],data["producer"],data["gender"],data["classification"])
    if(type=="book"):
        item:Book=Book(data["name"],data["yearpublication"],data["condition"],data["saleprice"],data["rentalprice"],data["invunits"],data["writer"],data["gender"],data["editorial"])
    if(type=="video"):
        item:Video=Video(data["name"],data["yearpublication"],data["condition"],data["saleprice"],data["rentalprice"],data["invunits"],data["creator"],data["gender"])
    
    item.getData()
    myconeccion.insertDBitem(data,type)

    return {
        "title": "Dato insertado en la DB"
    }


@app.route("/payment/<type>", methods=["POST"])
def createPayment(type):
    data = json.loads(request.data)


    if(type=="cash"):
        payment:Cash= Cash(data["identification"], data["value"])
    
    payment.getData()
    myconeccion.insertDBPayment(data,type)

    if(type=="creditcard"):
        payment:CreditCard= CreditCard(data["identification"], data["expirationdate"], data ["digits"], data ["quotas"])
    
    payment.getData()
    myconeccion.insertDBPayment(data,type)


    return {
        "title": "Dato insertado en la DB"
    }