
import numpy as np

def extract_data(filename):
    temps = []
    infile = open(filename, 'r')
    lines = infile.readlines()[1:] #skipping header
    for line in lines:
        lin_list = line.split() #list of each element in line
        #print(lin_list)
        for m in lin_list:
            m= float(m) #converting temps to floats
            temps.append(m)
    return temps

oct_2014 = extract_data("temp_oct_2014.txt")
oct_1945 = extract_data("temp_oct_1945.txt")


print(f"The average temperature for october 1945 was {np.mean(oct_1945):0.4f} celsius degrees ")
print(f"The maximum temperature for october 1945 was {np.max(oct_1945)} celsius degrees")
print(f"The minimum temperature for october 1945 was {np.min(oct_1945)} celsius degrees")
print()
print(f"The average temperature for october 2014 was {np.mean(oct_2014):0.4f} celsius degrees ")
print(f"The maximum temperature for october 2014 was {np.max(oct_2014)} celsius degrees")
print(f"The minimum temperature for october 2014 was {np.min(oct_2014)} celsius degrees")

"""
Run example:
user$ python3 temp_read_write.py

The average temperature for october 1945 was 6.5065 celsius degrees
The maximum temperature for october 1945 was 11.6 celsius degrees
The minimum temperature for october 1945 was 2.1 celsius degrees

The average temperature for october 2014 was 8.8548 celsius degrees
The maximum temperature for october 2014 was 13.6 celsius degrees
The minimum temperature for october 2014 was 2.3 celsius degrees


"""
#b)

def write_formatting(filename, list1, list2):
    outfile = open(filename, 'w')
    for g,h in zip(list1,list2):
        g = str(g) #converting to string before writing to new formatted txt file
        h = str(h)
        outfile.write(g+"  "+ h + '\n') #writing columns to file
    outfile.close()

b = write_formatting("temp_formatted.txt",oct_1945,oct_2014)

#Please find attached the output file "temp_formatted.txt"
