f=input("enter a file name with it's extention:")
try:
    h=open(f)
except:
    print("file>>",f,"doesn't exist\a\a\a")
    quit()
r=h.read()
print(r)
print("\n>>>the number of characters in",f,"file are",len(r))
input()