def fxn(stng):
    oupt = stng[0]
    for i in range(1, len(stng)):
        if stng[i-1] == ' ':
            oupt += stng[i]
    oupt = oupt.upper()
    return oupt
str=input("enter to generate acronym:-")
print(fxn(str))