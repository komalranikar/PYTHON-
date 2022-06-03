#Count characters, words and lines in a text file.
#program to print no. of lines present in the file.
fh=open(r"C:\Users\komal\Documents\komal.txt","r")
a=fh.readlines()
lc=0
for i in a:
    lc+=1
print("No. of lines in the text file:-",lc)
fh.close()

#program to print no. of words present in the file.
f=open(r"C:\Users\komal\Documents\komal.txt","r")
a=f.read()
word=a.split()
wc=0
for i in word:
    wc+=1
print("No. of words in the text file:-",wc)
f.close()

#program to print no. of characters present in the file.
file=open(r"C:\Users\komal\Documents\komal.txt","r")
a=file.read()
cc=0
for i in a:
    if i.isalpha():
        cc+=1
print("No. of characters in the text file:-",cc)

