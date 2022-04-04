#Write a program to check whether inputted no. is positive, negative and neutral value

num=int(input("enter thenumber to be checked:-"))
if num>0:
  print(num,"is a positive value")
elif num<0:
  print(num,"is a negative value")
elif num==0:
  print(num,"is a neutral value")
else:
  print("invalid input")