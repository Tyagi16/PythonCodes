Name = input("Enter your name")
print("Welcome", Name)

print ("Choose an option")
print ("1. For Addition of numbers")
print ("2. For subtraction of numbers")
print ("3. For multiply of numbers")
print ("4. For divide of numbers")

choose = input(" Choose an option 1/2/3/4:" )
def divide(a, b):
    return a/b
def add(a, b):
    return a+b
def sub(a, b):
    return a-b
def mul(a, b):
    return a*b
if choose == "1":
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    
    result = add(num1, num2)
    print("The sum of numbers: ", result)


elif choose == "2":
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    
    result = sub(num1, num2)
    print("The subtraction of numbers: ", result)



elif choose == "3":

    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    
    result = mul(num1, num2)
    print("The multiply of numbers: ", result)

elif choose == "4":

    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    
    result = divide(num1, num2)
    print("Divide of numbers: ", result)
else: 
    print("Invalid Choice") 


