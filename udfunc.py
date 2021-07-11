def computepay(h,r):
    if(h>40):
        gp=(40*r)+((h-40)*1.5*r)
    else:
        gp=h*r
    return(gp)
hrs = input("Enter Hours:")
rate = input("Enter rate per hour:")
ih = float(hrs)
ir = float(rate)
p = computepay(ih,ir)
print("Pay",p)