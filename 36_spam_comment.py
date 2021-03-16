Comment=input("Enter your comment here:\n")

if("click here to earn money" in Comment):
    spam=True
elif ("Buy this" in Comment):
    spam=True
elif ("Get $650,000$ by one tap or click" in Comment):
    spam=True
elif ("Earn money" in Comment):
    spam=True
else:
    spam=False
if(spam):
    print('THIS IS SPAM')
else:
    print('THIS IS NOT A SPAM')

