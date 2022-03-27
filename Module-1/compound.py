p=int(input("enter the principle value:-"))
r=float(input("enter the rate:-"))
t=int(input("enter the number of years:-"))
for i in range(t):
  c=p*(pow((1+r/100),t))
print(c)

#output
'''
enter the principle value:-1000
enter the rate:-5
enter the number of years:-2
1102.5

'''