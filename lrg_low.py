largest = None
smallest = None
print("type **do** when finished")
while True:
    num = input("Enter a number: ")
    if num == "do" : break
    try:
        n=int(num)
    except:
        print('Invalid input\a\a')
        continue
    if (largest==None)and(smallest==None):
        largest=n
        smallest=n
    else:
        if (n>largest):
            largest=n
        if (n<smallest):
            smallest=n
print("Maximum is",largest)
print("Minimum is",smallest)