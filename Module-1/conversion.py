print("type 'a' if you want to convert units of time.\n\
  type 'b' if you want to convert units of distance.\n\
  type 'c' if you want to convert units of temperature. ")
ch=input("enter your choice---")

if ch=="a":
  time=int(input("enter the time in minutes:-"))
  ctime=time/60
  print("Time in hours:-",ctime,"hrs.")

elif ch=='b':
  dist=int(input("enter the distance in meters:-"))
  cdist=dist/1000
  print("distance in kilometers:-",cdist,"kms")

elif ch=='c':
  temp=int(input("enter the temperature in celcius:-"))
  ctemp=temp+273
  print("temperature in kelvin:-",ctemp,"K")

#output

'''
type 'a' if you want to convert units of time.
  type 'b' if you want to convert units of distance.
  type 'c' if you want to convert units of temperature. 
enter your choice---a
enter the time in minutes:-180
Time in hours:- 3.0 hrs.

'''