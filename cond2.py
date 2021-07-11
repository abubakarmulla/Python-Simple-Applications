# two way conditional statement if/else 
ns=input("enter a integer: ")
ni=int(ns)
if (ni>=0):
    if (ni==0):
        print("it's a neutral zero\a")
    else:
        print("it's a positive integer")
else:
    print("it's a negative integer")