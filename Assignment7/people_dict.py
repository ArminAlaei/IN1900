
# Problem 7.6. Saving information in a nested dictionary

#a)
def read_person_data(filename):
    name = {}
    with open(filename) as infile:
        for line in infile:
            words = line.split()
            clean_name = words[0].strip(",")
            #creating nested dictionary
            data ={'Age': int(words[1].strip(",")), 'Gender':str(words[2])}
            name[clean_name] = data
    return name

dict_names = read_person_data("names.txt")
print(dict_names)

#b)
def write_person_data(data_dict, filename):
    outfile = open(filename, "w")
    for key in data_dict.keys():
        outfile.write(key + ", " + str(data_dict[key]["Age"]) +", "+ data_dict[key]["Gender"]+"\n")

    outfile.close()
    print(f"{filename} created in the same directory as the code")
write_person_data(dict_names, "outfile.txt")

"""
Run example:

user$ python3 people_dict.py

output:

{'John': {'Age': 55, 'Gender': 'Male'}, 'Toney': {'Age': 23, 'Gender': 'Male'},
'Karin': {'Age': 42, 'Gender': 'Female'}, 'Cathie': {'Age': 29, 'Gender': 'Female'},
'Rosalba': {'Age': 12, 'Gender': 'Female'}, 'Nina': {'Age': 50, 'Gender': 'Female'},
'Burton': {'Age': 16, 'Gender': 'Male'}, 'Joey': {'Age': 90, 'Gender': 'Male'}}

outfile.txt created in the same directory as the code


"""
