num=int(input("enter 3 digit number to be checked:-"))
sum=0
n=num
while n!=0:
  rem=n%10
  sum=sum+rem**3
  n=n//10
if num==sum:
  print(num,"is an armstrong number.")
else:
  print(num,"is not an armstrong number.")