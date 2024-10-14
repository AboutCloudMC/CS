#8. Ask the user to enter their forename, take each character in the name and move the value of the character 2 places to the right - output the new name. i.e. "CAT" = "ECV"  (Look up ASCII and these functions chr() and ord()
#9. Ask the user to enter the name the algorithm above has outputted and then return the original name to the user.

name = input("Please enter your forename: ")
nameDec = [] 

for i in range(len(name)):
    nameDec[i] = ord(name[i])

print(nameDec)