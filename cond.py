#first program using conditional statement
try:
    ns=int(input("enter a number: "))
    if (ns<0):
        print("given number is negative")
    elif (ns>0):
        print("given number is positive") 
    elif (ns==0):
        print("given number is neutral zero")
except:
    print("input error!!!\a")