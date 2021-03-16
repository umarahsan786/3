text=(input("Enter a text here\n"))
if('buy this'in text):
    spam=True
elif('pubg hack coc hack avaliable here'in text):
    spam=True
elif('one click to earn $650,000'in text):
    spam=True
elif('one tap to earn $650,000'in text):
    spam=True
else:
    spam=False
if(spam):
    print('this is a spam')
else:
    print('this is not a spam')