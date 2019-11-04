"""
PROGRAM: trap.py
Calculate trap resonate frequency based on coil inductance based on coil dimensions and capacitor value.  The inductance formula assumes a relative permiability
of air as a value of 1.  

"""

from math import pi,sqrt


diameter=float(input("Enter coil diameter in inches:"))
L=float(input("Enter length of coil in inches:"))
N=float(input("Enter number of turns in coil:"))
capValue=input("Enter capacitor value in pF:")

if capValue == "":												#default to 100 pF
	capValue=100
pF=float(capValue)												#convert capValue from string to float

inductance=(diameter**2) * (N**2) / ((18*diameter) + (40 * L))  #calculate inductance

FARAD=pF*10**-12												#convert pF to Farads for LC formula
HENRY=inductance/10**6											#convert uH to Henries for LC formula
freq=1/(2*pi*sqrt(HENRY*FARAD))                                 #resonant circuit formula


mhz=freq*10**-6											    	#convert hertz to megahertz
radius=diameter/2
circumference=2*pi*radius
wire_length=(circumference*N)/12

dec_inches=str(wire_length-int(wire_length))[1:]
inches=float(dec_inches)
inches=(inches*12)

feet=round(wire_length)
inches=round(inches)

#print(radius)
#print (circumference)
#print(wire_length) 
#print(inches)


print("\n\n")
print ('COIL INDUCTANCE = %0.3f uH'%inductance)
print ('FREQUENCY = %0.3f MHZ'%mhz)
print ('WIRE LENGTH = %0.3f' %wire_length)
print ('WIRE LENGTH = ' + (str(feet) +' FEET ' + str(inches) + ' INCHES '))






