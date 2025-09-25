def greet():
    print("Welcome to python functions!")
greet()

def greet_user(name):
    print("Hello",name)
greet_user("hero")

def greet(name="Guest"):
    print("Hello,",name)
greet()


x=100
def func():
    y=50
print("Inside function,X=",x)
    #access global
print("Inside function,Y=",y)
    #access 
func()
print("Outside function,X=",x)

n1=int(input("enter first number"))
n2=int(input("enter second number"))
def mul_numbers(a,b):
    return a*b
result=mul_numbers(n1,n2)
print(result)