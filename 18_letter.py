letter='''Dear NAME
    DATE
         From
              "Dear Omar Ahsan Khan, from abc house we are promoting you for your performance this year
               our regards have a good day.
                                            Thank you,from bill'''
Name = input('your name') 
Date = input('date')
From = input('From')
letter =letter.replace('NAME',Name)
letter =letter.replace('DATE',Date)
letter =letter.replace('From',From)
print (letter)                                                      
        