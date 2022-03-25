num1=int(input("Enter first number."))
num2=int(input("Enter second number."))
op=input("Enter the operation you want to do\n\
         + for addition\n\
         - for subtraction\n\
         * for multiplication\n\
         / for division\n\
         % for remainder.\n")
if op=='+':
    print(num1+num2)
elif op=="-":
    print(num1-num2)
elif op=="*":
    print(num1*num2)
elif op=="/":
    print(num1/num2)
elif op=="%":
    print(num1%num2)
else:
    print("Invalid operator.")