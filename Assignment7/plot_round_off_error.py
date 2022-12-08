
# Problem 7.5. Interpret output from a program
import numpy as np
import matplotlib.pyplot as plt

def plot_round(filename):
    delta_x = []
    abs_error = []
    n_list = []
    with open(filename, 'r') as infile:
        lines = infile.readlines()

        for line in lines:
            pa = line.strip()
            pl = pa.split(",")

            #choosing columns we want
            delt = pl[0]
            abe = pl[3]
            ne = pl[5]

            #getting values from each column
            de = delt.split(":")
            delta_x.append(float(de[1]))

            er = abe.split(":")
            abs_error.append(float(er[1]))

            en = ne.split("=")
            n_list.append(int(en[1]))
        infile.close()
        #converting the lists to numpy arrays
        deltax = np.array(delta_x)
        abserror = np.array(abs_error)
        n = np.array(n_list)

        #creating plot with logarithmic y axis
        plt.semilogy(n, deltax, label="Delta_x")
        plt.semilogy(n,abserror ,label="Abs_error")
        plt.legend()
        plt.show()
    #returning the three arrays
    return deltax, abserror,n

svar = plot_round("out.txt")
print(svar)

"""
Vi har at maskinpresisjon er 10^(-16) og for lavere verdier av delta_x så er f(x+delta_x)-f(x) nær null, og for
10^(-8) så er denne differensansen større enn maskinpresisjonen, men den er liten nok til at vi får en liten feil/
unøyaktighet. Når vi da deler på delta_x får vi en større unøyaktighet og vi ser at for approksimasjonen av den deriverte
når dx er 10^(-16) så får vi et helt feil tall. På grafen ser vi enkelt hvordan unøyaktigheten øker fra n = 8. Dette
fenomenet som oppstår her kalles round off error.


Run example:

user$ python3 plot_round_off_error.py

output:

(array([1.e-01, 1.e-02, 1.e-03, 1.e-04, 1.e-05, 1.e-06, 1.e-07, 1.e-08,
       1.e-09, 1.e-10, 1.e-11, 1.e-12, 1.e-13, 1.e-14, 1.e-15, 1.e-16,
       1.e-17, 1.e-18, 1.e-19]), array([4.409811e-02, 4.338424e-03, 4.330960e-04, 4.330210e-05,
       4.330133e-06, 4.331391e-07, 4.300676e-08, 3.038736e-09,
       4.137019e-08, 4.137019e-08, 4.137019e-08, 4.445029e-05,
       3.996389e-04, 1.150187e-02, 5.511151e-02, 5.000000e-01,
       5.000000e-01, 5.000000e-01, 5.000000e-01]), array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17,
       18, 19]))

Please find plot attached.
"""
