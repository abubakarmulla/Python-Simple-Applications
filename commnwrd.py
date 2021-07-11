fname=input("Enter file name:")
fh=open(fname)
count=dict()
for line in fh:
    if not line.startswith("From "):
        continue
    words=line.split()
    count[words[1]]=count.get(words[1],0)+1
val=max(count.values())
print(val)
for key in count:
    if count[key]==val:
        print(key,count[key])
input()