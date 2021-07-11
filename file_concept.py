fname = input("Enter file name: ")
fh = open(fname)
count=0
add=0
for line in fh:
    line=line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    count=count+1
    i=line.find('0')
    a=line[i:]
    add=add+float(a)
avg=add/count
print("Average spam confidence:",avg)