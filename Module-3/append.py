#append text to a file and display the text
f=open(r"C:\Users\komal\Documents\komal.txt","a")
print("Enter the text you want to append")
a=input()
f.write(a)
f.close()

fh=open(r"C:\Users\komal\Documents\komal.txt","r")
print(fh.read())
fh.close()