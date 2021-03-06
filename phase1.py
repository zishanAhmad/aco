# Phase 1:
# Initial S box generation using Chaotic Logistic Map and Tent Map
# Chaotic Logistic Map: x[i+1] = ux[i](1-x[i])
# Tent Map: x[i+1] = x[i]/b,           0 < x[i] <=b
#                    (1-x[i])/(1-b),   b < x[i] < 1
# x0 = 15961/29589
# u  = 3.999
# b  = 0.499


from decimal import *
from math import floor
from functions import *
from performance import *

def generate_sbox():    
    # Set precision to 15
    getcontext().prec = 15

    # Define intital/constant values
    num = 20821
    den = 27729
    x = Decimal(num)/Decimal(den)
    u  = Decimal(3999)/Decimal(1000)
    b = Decimal(4999)/Decimal(10000)
    print(x,u,b)
    # To counter Transient Effect
    # Iterate over Chaotic Logistic Map
    x = chaotic(x, u, 50)
    #print(x)

    # Iterate over Tent Map
    x = tent(x, b, 50)
    #print(x)

    # Generate S Box
    s = []
    while len(s) < 256:
        x = chaotic(x, u, 24) #25
        x = tent(x, b, 14) #14 
        #n = int(floor(256*x))
        n = int((float(x*(10**6)) - floor(x*(10**6)))*256)
        if n not in s:
            #print(len(s))
            #print(s)
            s.append(n)
    return s


if __name__ == '__main__':
    nn = []
    s = generate_sbox()    
    print(pretty(s))
    print(is_bijective(s))
    print(differential_probability(s))
    nn.append(nonlinearity(s))
    max_non=max(nn)
    print(max_non)