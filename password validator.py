print("* Instructions: this is a password validating application\n")
print("* Coditions that should satisfy in your password for successfull validation:-")
print("     1) you must use atleast 1 uppercase letter")
print("     2) you must use atleast 1 lowercase letter")
print("     3) you must use atleast 1 integer\n\n\n")
T = int(input("enter how many passwords you want to validate: "))
pwd = list()
out = dict()
for i in range(T):
    pwd.append(input("enter your password: "))
    
count=0
for cm in pwd:
    flag = 0
    integer=0
    up=0
    low=0
    count += 1
    for a in range(len(cm)):
        try:
            if(type(int(cm[a])) is int):
                flag += 1
                integer += 1
                continue
        except:
            if(cm[a].isupper() is True):
                flag += 1
                up += 1
                continue
            elif(cm[a].islower() is True):
                flag += 1
                low += 1
                continue
    if(integer > 0 and up > 0 and low > 0):
        out[count] = "password is validated successfully"
    else:
        out[count] = "password is invalid, validation failed!!"
        
print("Your 1st",out[1])
print("Your 2nd",out[2])
print("Your 3rd",out[3])

for key,value in out.items():
    if(key > 3):
        print("Your ",key,"th ",value)
        
input("")
