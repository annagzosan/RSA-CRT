# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 14:40:24 2021

@author: user
"""

import random
import math
from egcd import egcd
 
def power(x, y, p):
    res = 1;
    x = x % p;
    while (y > 0):
        if (y & 1):
            res = (res * x) % p;
        y = y>>1;
        x = (x * x) % p;
     
    return res;
 
def miillerTest(d, n):

    a = 2 + random.randint(1, n - 4);
 

    x = power(a, d, n);
 
    if (x == 1 or x == n - 1):
        return True;
 
    while (d != n - 1):
        x = (x * x) % n;
        d *= 2;
 
        if (x == 1):
            return False;
        if (x == n - 1):
            return True;
 
    return False;

def isPrime( n, k):
   
    if (n <= 1 or n == 4):
        return False;
    if (n <= 3):
        return True;
 

    d = n - 1;
    while (d % 2 == 0):
        d //= 2;
 
 
    for i in range(k):
        if (miillerTest(d, n) == False):
            return False;
 
    return True;

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('No modular inverse')
    return x%m




'''KEY GENERATION'''
p=0
q=0
k=4
for i in range(1000):    
    n=random.randint(1,pow(10, 5))
    f=abs(pow(n, 2)+n-1354363)
    if (isPrime(f, k)):
        if (p==0):
            p=f
            continue
        if (p!=f and q==0):
            q=f
            break
n=p*q  
f=(p-1)*(q-1)
e=0     
for i in range(2,f):
    if math.gcd(i,f)==1:
        e=i
        break
d=modinv(e, f)
dP=(1/e)%(p-1)
dQ=(1/e)%(q-1)
qInv=(1/q)%p

    
 


'''ENCRYPTION'''
c=math.pow(m, e)%n
print(int(c))

'''DECRYPTION'''
# m = c^d mod n
#from the CRT => x=a mod pq IF AND ONLY IF x=a mod p AND x=a mod q
#m=c^d mod p and m=c^d mod q
#in the place of c we can use c%p/q

m1=math.pow(c, dP)%p
m2=math.pow(c, dQ)%q
h=qInv*(m1-m2)%p
m_original=m2+h*q
print(int(round(m_original)))



