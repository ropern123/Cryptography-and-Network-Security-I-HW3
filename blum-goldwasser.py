from math import log, floor


p=499
q=547
a=-57
b=52
X0=159201
m=0b10011100000100001100

print('The original message is    ', bin(m)[2:])

n=p*q


k = floor(log(n,2))
h = floor(log(k,2))
mask = (1 << h) - 1

t = m.bit_length() // h + (1 if m.bit_length() % h != 0 else 0)

m2 = m
X = X0
c = 0
for i in range(1, t + 1):
    X = pow(X, 2, n)
    pi = X & mask
    mi = m2 & mask
    c |= (mi ^ pi) << (h*(i-1))    
    m2 >>= h


c |= pow(X, 2, n) << (h*t)


print('The ciphertext is', bin(c)[2:])


d1 = pow((p+1)//4, t + 1, p - 1)
d2 = pow((q+1)//4, t + 1, q - 1)

u = pow(c >> (h*t), d1, p)
v = pow(c >> (h*t), d2, q)

X = (v*a*p + u*b*q ) % n
mm = 0
for i in range(1, t + 1):
    X = pow(X, 2, n)
    mm |= ( ((c >> (h*(i-1))) & mask) ^ (X & mask) ) << (h*(i-1))

print('The decrypted ciphertext is', bin(mm)[2:])

assert mm == m