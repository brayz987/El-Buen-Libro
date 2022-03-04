from Mysql import Mysql
from ..domain.Persons.Client import Client


mysql:Mysql=Mysql("127.0.0.1","elbuenlector","Brayan711737","3306","root")
mysql.connect()
p1:Client = Client('Brayan','Cardenas',20,'CC',1000322539,3502342132)
p1.getData()
# p1.insertDB({
    
#     "name":"{p1.name}",
#     "lastname":"Cardenas",
#     "age":20,
#     "typeidentification":"CC",
#     "identification":1003706375,
#     "phone":3502649117

# },"clients")


print({
    
    "name":"{p1.name}",
    "lastname":"Cardenas",
    "age":20,
    "typeidentification":"CC",
    "identification":1003706375,
    "phone":3502649117

},"clients")