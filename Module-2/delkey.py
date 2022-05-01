d={'a':1,'b':2,'c':3,'d':4,'e':5}
key=input("enter the key to be deleted:-")
if key in d: 
    del d[key]
else:
    print("Key not found!")
    exit(0)
print(d)