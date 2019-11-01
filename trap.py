"""
PROGRAM: trap.py
Calculate trap resonate frequency based on coil inductance based on coil dimensions and capacitor value.  The inductance formula assumes a relative permiability
of air as a value of 1.  

"""

from math import pi,sqrt


diameter=float(input("Enter coil diameter in inches:"))
N=float(input("Enter number of turns in coil:"))
L=float(input("Enter length of coil in inches:"))
capValue=input("Enter capacitor value in pF:")

if capValue == "":												    #default to 100 pF
	capValue=100
pF=float(capValue)													#convert capValue from string to float

inductance=(diameter**2) * (N**2) / ((18*diameter) + (40 * L))

FARAD=pF*10**-12												#convert pF to Farads for LC formula
HENRY=inductance/10**6											#convert uH to Henries for LC formula
freq=1/(2*pi*sqrt(HENRY*FARAD))
print (FARAD)
print (HENRY)
print(freq)
mhz=freq*10**-6											    	#convert hertz to megahertz


print("\n\n")
print ('COIL INDUCTANCE = %0.3f uH'%inductance)
print ('FREQUENCY = %0.3f MHZ'%mhz)







