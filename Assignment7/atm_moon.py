
#Problem 7.4. Use string operations to create a pretty dictionary
moon = {}
with open('atm_moon.txt', 'r') as infile:
    lines = infile.readlines()[1:] #skipping header
    for line in lines:
        a = line.strip() #stripping leading and trailing characters
        b = a.split(";")
        for el in b:
            c = el.split(" - ")
            navn = c[0].strip()
            navn = navn.upper()
            verdi = c[1]
            vb = verdi.replace(",","")
            vb = float(vb)
            moon[navn]= vb

#Printing in the same format as in the task
for m in moon.keys():
    print(f"´{m}´ : {moon[m]}")


"""
Run example:

user$ python3 atm_moon.py

output:

´HELIUM 4´ : 40000.0
´NEON 20´ : 40000.0
´HYDROGEN´ : 35000.0
´ARGON 40´ : 30000.0
´NEON 22´ : 5000.0
´ARGON 36´ : 2000.0
´METHANE´ : 1000.0
´AMMONIA´ : 1000.0
´CARBON DIOXIDE´ : 1000.0
"""
