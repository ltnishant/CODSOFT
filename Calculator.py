def add (x,y):
    return x+y
def subtract (x,y):
    return x-y
def multiply (x,y):
    return x*y
def divide (x,y):
    return x/y

# x=int(input("Enter a First Number : "))
# y=int(input("Enter a Second Number : "))

print (" 1 --- ADDITION  "
       "2 --- SUBSTRACTION  "
       "3 --- MULTIPLICATION  "
       "4 --- DIVISION  ")

choice = int(input("Enter Your Choice : "))
while choice>0 :
    if choice == 1:
        x = int(input("Enter a First Number : "))
        y = int(input("Enter a Second Number : "))
        print (add(x,y))
    elif choice == 2:
        x = int(input("Enter a First Number : "))
        y = int(input("Enter a Second Number : "))
        print(subtract(x,y))
    elif choice == 3:
        x = int(input("Enter a First Number : "))
        y = int(input("Enter a Second Number : "))
        print(multiply(x,y))
    elif choice == 4:
        x = int(input("Enter a First Number : "))
        y = int(input("Enter a Second Number : "))
        print(divide(x,y))
    else:
        print ("Invalid Choice")
def add(x, y):
  return x + y

def subtract(x, y):
  return x - y

def multiply(x, y):
  return x * y

def divide(x, y):
  return x / y


