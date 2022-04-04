num=int(input("enter the number to reverse:-"))
rev=0
while num>0:
  rem=num%10
  rev=(rev*10)+rem
  num=num//10
print("reversed number:-",rev)