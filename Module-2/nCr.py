def fact(num):
  f=1
  if num>=0:
    for i in range(1,num+1):
      f=f*i
      i+=1
  return f

n=int(input())
r=int(input())
ncr=fact(n)/(fact(r)*fact(n-r))
print(ncr)