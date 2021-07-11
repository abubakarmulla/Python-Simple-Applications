fname=input("enter file name")
fh=open(fname)
d=dict()
for line in fh:
    if not line.startswith("From "):
        continue
    words=line.split()
    hr=words[5].split(':')
    d[hr[0]]=d.get(hr[0],0)+1
lst=d.items()
for k,v in sorted(lst):
    print(k,v)