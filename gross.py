hrs = input("Enter Hours:")
rph = input("Enter rate per hour")
fh=float(hrs)
fr=float(rph)
if(fh<=40.0):
    gross=(fh*fr)
elif(fh>40.0):
    gross=(40*fr)+((fh-40)*1.5*fr)
print(gross) 