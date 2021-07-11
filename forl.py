lst = list()
while True:
    a=input("")
    if(a==''):
        break
    elif(type(a)!=int):
        continue
    lst.append(int(a))
try:
    lrg=lst[0]
    for i in lst:
        if(i>lrg):
            lrg=i
    print("largest data is : ",lrg)
except:
    print("invalid data entered!!\a")
input()