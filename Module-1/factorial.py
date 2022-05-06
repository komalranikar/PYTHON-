num=int(input("Enter the number:-"))
f=1
if num>=0:
  for i in range(1,num+1):
    f=f*i
    i+=1
print("Factorial of",num,"is",f)


#output

'''
Enter the number:-5
Factorial of 5 is 120

'''