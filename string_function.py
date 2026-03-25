'''Some of the common string function are.'''

str = input("Enter a string : ")

print(str.endswith("substring"))     #return true if string ends with substring else false
print(str.capitalize())              #capitalize first char
print(str.replace("old","new"))      #replaces all occurrency of old with new
print(str.find("word"))              #return 1st index of 1st time occurence of the word
print(str.count("substring"))        #counts the occurence of substring in the string