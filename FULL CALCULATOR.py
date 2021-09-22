#This function adds two numbers
def add(x,y):
    return x + y
#this function subtracts two numbers
def subtract(x,y):
    return x - y
#This function multiply two numbers
def multiply(x,y):
    return x * y
#This function two numbers
def divide(x,y):
    return x / y

print("SELECT OPERATION")
print("1.ADD")
print("2.SUBTRACT")
print("3.MULTIPLY")
print("4.DIVIDE")
while True:
    choice=input('Enter Choice(1/2/3/4): ')
    #take input from user
    #check if choice in one of given
    if choice in ('1,2,3,4'):
        num1=float(input("Enter your first number: "))
        num2=float(input("Enter your second number: "))

        if choice =="1":
            print(num1,"+",num2,"=",add(num1,num2))

        elif choice=="2":
            print(num1,"-",num2,"=",subtract(num1,num2))

        elif choice=="3":
            print(num1,"*",num2,"=",multiply(num1,num2))

        elif choice=="4":
            print(num1,"/",num2,"=",divide(num1,num2))


        next_calculation=input("Let's do another calculation(yes,no): ")
        if next_calculation == "no":
            break

    else:
        print("INVALID INPUT")