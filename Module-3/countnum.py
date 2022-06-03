#Read numbers from a file and write even and odd numbers to separate files.
file=open(r"C:\Users\komal\Documents\komal.txt","r")
a=file.read()
cc=0
for i in a:
    if i.isnumeric():
        cc+=1
print("No. of characters in the text file:-",cc)