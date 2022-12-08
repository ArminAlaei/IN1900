
#8.1. Saving information in a class

class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def newname(self,newname):
        self.name = newname

    def newage(self,newage):
        self.age = newage

    def newgender(self, newgender):
        self.gender = newgender

    def __str__(self):
        return f"{self.name}, {self.age}, {self.gender}"

pers = Person("John",25,"Male")
print(pers)

nyNavn = pers.newname("Joanna") #Using the methods to change a persons name etc.
nyKj = pers.newgender("Female")

print(pers)

"""
Run example:

user$ python3 class_people.py

output:
John, 25, Male
Joanna, 25, Female


"""
