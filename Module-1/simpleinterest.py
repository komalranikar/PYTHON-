#Write a program to calculate simple interest.

p=int(input("enter the principle value:-"))
r=float(input("enter the rate:-"))
t=int(input("enter the number of years:-"))
si=(p*r*t)/100
print("simple interest:-",si)