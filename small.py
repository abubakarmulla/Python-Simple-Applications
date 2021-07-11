small=None
for a in [34,45,56,99,4,5,2,55,67,38]:
    if small==None:
        small=a
    elif a<small:
        small=a
print('smallest value=',small)