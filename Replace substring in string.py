def replace_substring(string,old,new):
    return string.replace(old,new)
string=input("Enter the main string : ")
old=input("Enter the word to replace : ")
new=input("Enter the new word : ")
print("Updated String : ",replace_substring(string,old,new))
