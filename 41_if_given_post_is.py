sent=('ahsan','omer','king')
a = (input("Enter a word you want to find:\n"))
if(a.lower in sent):
    print("it is in the list")
else:
    print("it is not in the list")