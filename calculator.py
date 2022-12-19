def sum():
    a=int(input("Enter the first number:"))
    b=int(input("Enter the second number:"))
    return a+b
def sub():
    a=int(input("Enter the first number:"))
    b=int(input("Enter the second number:"))
    return a-b
def div():
    a=int(input("Enter the first number:"))
    b=int(input("Enter the second number:"))
    c=a/b
    divide="{:.2f}".format(c)
    return divide
def mul():
    a=int(input("Enter the first number:"))
    b=int(input("Enter the second number:"))
    return a*b
print("------------------------------------")    
print("**select the operation to perform**")
print("------------------------------------")
print("1.Sum")
print("2.Subtract")
print("3.Division")
print("4.Multiply")

print("----------------")
while(True):
    i=int(input("Enter your Choice:"))
    if (i==1):
        print(sum())
    elif (i==2):
        print(sub())
    elif (i==3):
        print(div())
    elif (i==4):
        print(mul())
    else:
        print("wrong choice")
    cont =input("Do you want to continue? yes/no > ")
    while cont.lower() not in ("yes","no"):
        cont =input("Do you want to continue? yes/no > ")
    if cont == "no":
        print("Exit")
        break                