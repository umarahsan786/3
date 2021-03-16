sub1=int(input("Enter the marks in english: "))
sub2=int(input("Enter the marks in science: "))
sub3=int(input("Enter the marks in maths:" ))
if(sub1<33 or sub2<33 or sub3<33):
    print("You are failed in the exam due to low marks in the paper")
elif (sub1+sub2+sub3)/3<40:
    print("You are failed due to all papers are not clear")
else:
    print("Congragulations, You have passed these exam keep it up")
    