
# 5.7. Read isotope file
molar_mass = [] #empty list to store the calulated molar masses
infile = open('oxygen.txt', 'r') # open file
lines = infile.readlines()[1:] #Skipping first line since its the data header

#iterating through the lines
for line in lines:
    lin_list = line.split() #splitting into words

    weight = float(lin_list[2]) #converting from str to float for calculation
    nat_a = float(lin_list[3])
    mass = weight*nat_a
    molar_mass.append(mass)
infile.close() #closing file

#Printing out the calculated molar mass
for mol in molar_mass:
    print(f"{mol:.4f} g/mol")
