import random
r=random.randint(1,50)
while(True):
    n=int(input("Enter the number:"))
    if(n>r):
        print("Wrong guess, try smaller number")
    elif(n<r):
        print("Wrong guess, try larger number")  
    else:
        print("Congrats, you've guess the number")           
        break