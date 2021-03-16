# a=[3,34,1,55,23,49]
# print(34 in a)
# a =(True and False)
# b =(True and True)
# c =(False or True)
# c1 =(True or False)
# print(a,b,c1,c)
list1=[]
list2=[]
list3=list1
if(list1==list2):
    print(True)
else:
    print(False)
if(list1 is list2):
    print(True)
else:
    print(False)
if(list1 is list3):
    print(True)
else:
    print(False)