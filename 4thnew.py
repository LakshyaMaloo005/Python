def factorial(a):
    if a==1:
        return 1
    else:
        return( a*factorial(a-1))





def calling():
    z=int(input("enter a number"))
    b= print(factorial(z))


calling()
