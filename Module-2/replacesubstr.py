'''
14.	Program for Counting occurrence of a certain element in a string, getting indexes that have matching elements.For ex -.In Rabbit count how many times b has occurred . Example-I have to go to a doctor and get myself checked. Count the number of occurrences of ‘to’.

'''


a=input("enter the string:")
b=input("to be count:")
cou=0
li=[]
li=list(a.split(" "))
c=len(li)
print("len of the li",c)
if c==1:
    for i in range(0,len(a)):
        if a[i]==b:
            cou=cou+1
else:
    for i in range(0,len(li)):
        if li[i]==b:
            cou=cou+1
print(cou)