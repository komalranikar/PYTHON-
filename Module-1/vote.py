#Write a program to check whether person is eligible to vote or not

name=input("enter the name of the person:-")
age=int(input("enter the age of the person:-"))
if age>=18:
  print(name,"is eligible for voting.")
else:
  print(name,"is not eligible for voting.")