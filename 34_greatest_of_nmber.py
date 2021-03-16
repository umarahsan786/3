num1=int(input('Enter the 1st number: \n'))
num2=int(input('Enter the 2nd number: \n'))
num3=int(input('Enter the 3rd number: \n'))
num4=int(input('Enter the 4th number: \n'))
if (num1>num4):
    f1=num1
else:
    f1=num4
if (num2>num3):
    f2=num2
else:
    f2=num3
if (f1>f2):
    print (str(f1 ) + (" is the greatest number"))
else:    
    print (str(f2 ) + (" is the greatest number"))   



