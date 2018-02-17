number = int(input("Put in a number:"))
if number > 1:
        for x in range (2, number):
            if (number % x) == 0:
                print("This is not a prime number")
                break
        else: 
            print(number, "This is a prime number")
            
else:
    print(number, "This is not a prime number")
    