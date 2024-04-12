#without power
a=int(input("enter the base number"))
b=int(input("enter the power number"))
print(a**b)

#with power function
z=pow(a,b)
print(z)

#greatest common divison
c=int(input("enter the smallest number first"))
d=int(input("enter the largest number"))
v=d%c
if(v==0):
    print(c)
else:
    print("invalid")
    
#greatest common divison with maths function
import math
g=math.gcd(c,d)
print(g)
# or we can print by print(f[g])
