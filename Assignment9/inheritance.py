# Problem 9.4. Inheritance

class Mammal:
    def info(self):
        return "I have hair on my body"
    def identity_mammal(self):
        print("I am a mammal")

class Primate(Mammal):
    def info(self):
        return Mammal.info(self) + " and I have a large brain"
    def identity_primate(self):
        print("I am a Primate")

class Human(Primate):
    def info(self):
        return Primate.info(self) +" and im a human being "
    def identity_human(self):
        print("I am a Human")

class Ape(Primate):
    def info(self):
        return Primate.info(self) +" and im an ape "
    def identity_ape(self):
        print("I am an Ape")


print()
print("c)")
John = Human()
Julius = Ape()

print(Julius.info())
Julius.identity_mammal()
Julius.identity_primate()
#Julius.identity_human() #causes error as expected
Julius.identity_ape()
print()
print(John.info())
John.identity_mammal()
John.identity_primate()
John.identity_human()
#John.identity_ape()  #causes error causes error as expected

print()
print("d)")
print(isinstance(John, Mammal))
print(isinstance(John, Primate))
print(isinstance(John, Human))
print(isinstance(John, Ape))
print()
print(isinstance(Julius, Mammal))
print(isinstance(Julius, Primate))
print(isinstance(Julius, Human))
print(isinstance(Julius, Ape))

"""
Run example:

user$ python3 inheritance.py
output:


c)
I have hair on my body and I have a large brain and im an ape
I am a mammal
I am a Primate
I am an Ape

I have hair on my body and I have a large brain and im a human being
I am a mammal
I am a Primate
I am a Human

d)
True
True
True
False

True
True
False
True
"""
