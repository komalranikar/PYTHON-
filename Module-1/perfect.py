num=int(input("Enter the number:-"))
a=0
for i in range(1,num-1):
  r=num%i
  if r==0:
    a+=i
if num==a:
  print(num,"is a perfect number.")
else:
  print(num,"is not a perfect number.")

#outpt

'''
Enter the number:-6
6 is a perfect number.

'''