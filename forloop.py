name = input("Please enter your forename: ").lower()
newName = ""
for i in range(len(name)):
    newChr = ord(name[i])-2
    print(newChr)
    if newChr < ord("a"):
        newChr += 26
    
    newName += chr(newChr)
print(newName)