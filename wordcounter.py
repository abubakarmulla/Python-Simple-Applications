fname=input("Enter file name: ")
fh=open(fname)
names=dict()
for line in fh:
    if line=='\n':
        continue
    words=line.split()
    for i in words:
        names[i]=names.get(i,0)+1 #details of this statement is present below
#        if i in names:
#           names[i]=names[i]+1
#        else:
#           names[i]=1
val=names.values()
for op in names:
    print(op,'=',names[op])
    if names[op]==max(val):
        mx=[op,names[op]]
print("the word repeated maximum is**",mx[0],"**and it is repeated for",mx[1],"times in file",fname)
input()