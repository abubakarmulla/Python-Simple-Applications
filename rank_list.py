rank=dict()
while True:
    name=input("Name:")
    if name=="done":
        break
    marks=input("marks ")
    try:
        rank[name]=int(marks)
    except:
        print("no data given\a\a")
        exit()
print("rank list is as follows:")
lst=list()
for k,v in rank.items():
    lst.append((v,k))
i=0
for v,k in sorted(lst,reverse=True):
    i=i+1
    print(i,".",k,"   Marks==>",v)
if len(rank)==0:
    print("no data given\a\a")