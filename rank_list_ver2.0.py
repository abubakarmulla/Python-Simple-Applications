# owner of software ==> Abubakar Mulla
print("******created by==> Abubakar Mulla******")
rank=dict()
while True:
    name=input("Name:")
    if name=="done":
        break
    marks=input("marks ")
    try:
        rank[int(marks)]=name
    except:
        print("no data given\a\a")
        exit()
print("rank list is as follows:")
i=0
for v,k in sorted(rank.items(),reverse=True):
    i=i+1
    print(i,".",k,"   Marks==>",v)
if len(rank)==0:
    print("no data given\a\a")
input()