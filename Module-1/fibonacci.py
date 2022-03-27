num=int(input("Enter the number:-"))
t1=0
t2=1
t3=0
if num==0:
  print(num)
elif(num==1):
  print(num)
else:
  t3=t1+t2
  for i in range(3,num+1):
    t1=t2
    t2=t3
    t3=t1+t2
    print(t3)

#output

'''
Enter the number:-9
2
3
5
8
13
21
34

'''