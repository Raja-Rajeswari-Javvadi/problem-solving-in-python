import string
def remove_punctuation(text):
    punctuation=string.punctuation
    result=""
    for char in text:
        if char not in punctuation:
            result+=char
    return result
text=input("Enter text with punctuations : ")
cleaned_text=remove_punctuation(text)
print("Text after punctuation : ",cleaned_text) 

