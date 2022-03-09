from domain.Persons.Person import Person
from domain.Persons.Client import Client
from domain.Items.Movie import Movie
from domain.Records.Devolution import Devolution
from domain.Payments.DebitCard import DebitCard



# p1:Person = Person('Brayan','Cardneas',20,'CC',1000322539,3502342132,'Administrator')
# p1.getData()

# p1:Client = Client('Brayan','Cardenas',20,'CC',1000322539,3502342132)
# p1.getData()

# p1:Administrator = Administrator('Brayan','Cardenas',20,'CC',1000322539,3502342132)
# p1.getData()


# i1:Movie = Movie('Madagascar',2005,'Good',25000,5000,2,'Someone','Action',"7+")
# i1.getData()

# r1:Devolution = Devolution('Madagascar')
# r1.getData()

# p1:DebitCard = DebitCard("Brayan")
# p1.getData()



p1:Client = Client('Brayan','Cardenas',20,'CC',1000322539,3502342132)
p1.getData()
p1.insertDB()


