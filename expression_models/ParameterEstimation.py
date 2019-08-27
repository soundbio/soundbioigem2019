import numpy as np
import matplotlib.pyplot as plt
import random
import math

superscript = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹");
# when this is called, all the chars in the first argument turn into the corresponding ones in the second argument

def polyToStr(coefficients): # taking the coefficients, it builds the function's equation.
    degree=len(coefficients)-1;
    signs = [" " for x in range(degree+1)]
    xpowers = ["" for x in range(degree+1)]
    
    x=1;
    
    while x<degree+1: # ["", "x", "x", "x"...]
        xpowers[x] = xpowers[x] + "x";
        x=x+1;
    x=2;
    
    while x<degree+1: # adding powers to the 'x' s
        xpowers[x] = xpowers[x] + str(x).translate(superscript);
        x=x+1;

    x=0;

    # Deciding if the coefficients need a + sign or a - sign
    while x<degree+1:
        if coefficients[x] >= 0:
            if x==degree:
                signs[x] = " ";
            else:
                signs[x] = " + ";
        else:
            signs[x] = " - "
        x=x+1;

    x=degree;
    equation = "y =";
    
    coefficients=[round(x, 2) for x in coefficients]
    
    # Building an equation out of signs, coefficients and variables
    while x>=0:
        
        if (coefficients[x]==1 or coefficients[x]==-1) and x!=0:
            equation = equation + signs[x] + xpowers[x]; # doesn't write "1" as a coefficient
        elif coefficients[x]!=0: #will only add the term to the equation if it has a coefficient other than 0
            if coefficients[x]%1==0: # won't show decimals if not necessary
                equation = equation + signs[x] + str(abs(int(coefficients[x]))) + xpowers[x];
            else:
                equation = equation + signs[x] + str(abs(coefficients[x])) + xpowers[x];#adds the sign, then the coefficient, then the variable
        x=x-1;
    
    return equation;

def polyEval(x, coeffs):
    y=np.zeros(len(x)); # outputs of same length as inputs
    i=len(coeffs)-1;
    while i>=0: # starting from the highest power, moving down
        y=y+coeffs[i]*(x**i); # the same operation is done to all elements in y, for the corresponding x index
        i=i-1;
    return y;

def plot():
    
    yrough=polyEval(x, coeffs)
    
    plt.figure(1);
    plt.plot(x, y, label='input');
    plt.plot(x, yrough, label='approximation')
    plt.grid(True);
    plt.legend()
    plt.show()
    
    #print("\nThis is the graph of the function " + polyToStr(coeffs) + " :\n"); # FOR POLYNOMIALS

    print("coefficients are "+ str(coeffs))

def inputeval(x, coeffs):
    return [i for i in x] # THIS would be replaced by actual data

def neweval(x, coeffs):
    #return polyEval(x, coeffs)
    return [coeffs[0]+coeffs[1]*(coeffs[2]**coeffs[3]/(coeffs[2]**coeffs[3]+R(i-coeffs[4])**coeffs[3])) for i in x]

def Y(time):
    k1=0 # TO BE FILLED OUT 
    k2=0 # TO BE FILLED OUT 
    kdil=0 # TO BE FILLED OUT 
    kdr=0 # TO BE FILLED OUT 
    ktot=k1+k2+kdil+kdr
    y0=0
    return y0+(k1/ktot-y0)*(1-math.e**(-ktot*time))

def R(time):
    return Y(time)/(1-Y(time))

'''
TWEAKABLES:
    change these values, set a target function in inputeval, set a use for the coefficients in neweval (function)
    when using polynomials with the polyEval and PolyToStr functions, smallest power coefficients come first in arrays
'''

i=[0, 0, 0, 0, 0] # target function's coefficients, smallest to largest power's coefficient if polynomial
# this part will be replaced with real data
res=0.1
step=0.05
avgerrortolerance=0.0001
coeffnum=5 # a, b, K, n, T in order. maybe one or more can be experimentally determined (like a or b)
random.seed(1)

x=np.arange(0, 2+res, res) # the time axis
coeffs=np.zeros(coeffnum)

y=inputeval(x, i) # building the target function from coefficients
yrough =neweval(x, coeffs) # build approximation from existing coefficients (all set to 0)

length=len(y)

avgerror = sum([abs(y[x]-yrough[x]) for x in range(length)])
print(avgerror)
counter=0
temperror=0
coeffscopy=0
print(avgerror/length)

while abs(avgerror)/length>avgerrortolerance:
    
    coeffscopy=coeffs
    coeffs=[x+(random.random()-0.5)*2*step for x in coeffs]
    
    yrough=neweval(x, coeffs)
    
    temperror=sum([abs(y[x]-yrough[x]) for x in range(length)])
    
    if abs(temperror)>abs(avgerror):
        coeffs=coeffscopy
        
    else:
        avgerror=temperror
        
        print(avgerror/length)

yrough=polyEval(x, coeffs)

plt.figure(1);
plt.plot(x, y, label='input');
plt.plot(x, yrough, label='approximation')
plt.grid(True);
plt.legend()
plt.show()

#print("\nThis is the graph of the function " + polyToStr(coeffs) + " :\n"); # FOR POLYNOMIALS

print("coefficients are "+ str(coeffs))