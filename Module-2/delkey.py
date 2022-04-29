d = {'a':1,'b':2,'c':3,'d':4}
key=input("Enter the key to delete:")
if key in d: 
    del d[key]
else:
    print("Key not found!")
    exit(0)
print(d)