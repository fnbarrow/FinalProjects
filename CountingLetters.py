'''
Created on Nov 18, 2017

@author: ITAUser
'''
#open the text file
#read the file 
#split the file
#count the letters
#print result

def CountingLetters(filename, mychar):
   f = open(filename, 'r')
   count = 0;
   f.read('r')
   run = True
   while run:
       letter = f.read(1)
       letter = letter.lower()
       if letter == "":
        break 
    else: 
        if letter == mychar:
            count = count + 1
    print(count)
    
CountingLetters(filename="consitution.txt", mychar="a")

    