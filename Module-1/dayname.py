#Write a program to print day name corresponding to the inputted day no. Display appropriate error message too.

day=int(input("enter the day number:-"))
if day==1:
  print("It's Sunday")
elif day==2:
  print("It's Monday")
elif day==3:
  print("It's Tuesday")
elif day==4:
  print("It's Wednesday")
elif day==5:
  print("It's Thursday")
elif day==6:
  print("It's Friday")
elif day==7:
  print("It's Saturday")
else:
  print("Invalid day number.")