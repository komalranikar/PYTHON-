eng=int(input("enter the marks of english"))
math=int(input("enter the marks of maths"))
bio=int(input("enter the marks of biology"))
hindi=int(input("enter the marks of hindi"))
cs=int(input("enter the marks of comp. sc."))
total=eng+math+bio+hindi+cs
percent=total/5 
if percent>=90:
  print("Grade A")
elif percent>=80 and percent<90:
  print("Grade B")
elif percent>65 and percent<80:
  print("Grade C")
elif percent>50 and percent<65:
  print("Grade D")
elif percent>40 and percent<50:
  print("Grade E")
else:
  print("The student's percent is less than 40")
  print("FAILED")

#output

'''
enter the marks of english45
enter the marks of maths89
enter the marks of biology65
enter the marks of hindi76
enter the marks of comp. sc.45
Grade D
'''