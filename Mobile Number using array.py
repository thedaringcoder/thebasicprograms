def mobilenumbercheck(num):
    digits=[]
    while num!=0:
        d=num%10
        digits.append(d)
        num//=10
    if len(digits)==10:
        if digits[-1] in (7,8,9):
            print("Valid Mobile Number")
        else:
            print("Invalid Mobile Number")
    else:
        print("Invalid Mobile Number")

ph=int(input("enter a mobile number: "))
mobilenumbercheck(ph)