'''
Created on Dec 2, 2017

@author: ITAUser
'''
def CountingLetters(filename, mychar):
    f = open(filename, 'r')
    count = 0;
    run = True
    while run:
        letter = f.read(1)
        letter = letter.lower()
        if letter == "":
            break 
        else: 
            if letter == mychar:
                count = count + 1
    return(count)
CountingLetters(filename="constituton.txt", mychar="a")
CountingLetters(filename="constituton.txt", mychar="b")
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
countlist = []
for letter in letters:
    currentcount = CountingLetters("constituton.txt",letter)
    countlist.append(currentcount)
print(countlist)    
dracula = max(countlist)
print(dracula)   
indexletter = countlist.index(dracula)
largestletter = letters[indexletter]
print(largestletter)

