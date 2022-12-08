
#7.2 Chemical elements in a dictionary

elements_10 = {1: '-', 2: 'Helium', 3: 'Lithium',
4: 'Beryllium', 5: 'Boron', 6: 'Carbon',
7: 'Nitrogen', 8: '-',
9: 'Fluorine', 10: 'Neon'}

elements_10[1] = "Hydrogen"
elements_10[8] = "Oxygen"

elements_10_copy = elements_10.copy()
elements_10_copy.update({11: 'Sodium'})
print(elements_10)
print('\n')
elements_11 = elements_10
elements_11.update({11: 'Sodium'})
print(elements_10)



"""
#Den første printen i oppgave b) printer "gamle" elements_10
#listen, mens den andre printen kommer etter at elements_10 blir assignet til
#variabel navnet elements_11. Den andre printen er altså den oppdaterte versjonen
#av dictionariet.

{1: 'Hydrogen', 2: 'Helium', 3: 'Lithium', 4: 'Beryllium', 5: 'Boron', 6: 'Carbon', 7: 'Nitrogen', 8: 'Oxygen', 9: 'Fluorine', 10: 'Neon'}


{1: 'Hydrogen', 2: 'Helium', 3: 'Lithium', 4: 'Beryllium', 5: 'Boron', 6: 'Carbon', 7: 'Nitrogen', 8: 'Oxygen', 9: 'Fluorine', 10: 'Neon', 11: 'Sodium'}
"""
