def addition(x, y):
    sum = x + y
    print(f"the sum is {sum}")

def subtraction(x, y):
    difference = x - y
    print(f"the differnece is {difference}")

def division(x, y):
    quotient = x / y
    print(f"the quotient is {quotient}")

def multiplicatoin(x, y):
    multi = x * y
    print(f"the multiplciatoin is {multi}")

running = True

while running:
    response = input("would you like to add, subtract, multiply, diveide? (a,s,m,d)\n")

    print("format x (+,-,*,/) y")
    x = int(input("what is the x? \n"))
    y = int(input("what is the y? \n"))45


    if response == 'a':
        addition(x, y)
    elif response == 's':
        subtraction(x, y)
    elif response == 'm':
        multiplicatoin(x, y)
    elif response == 'd':
        division(x, y)
    elif response == 'q':
        running = False