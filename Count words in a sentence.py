def count_words(sentence):
    words=sentence.split()
    return len(words)
sentence=input("Enter the sentence : ")
print("Words count is ",count_words(sentence))