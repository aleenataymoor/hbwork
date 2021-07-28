import string
# import sys

# print(sys.argv)

def word_counter(file_name="test.txt"):
    open_file=open(file_name,"r")
    word_count={}
    for line in open_file:
        line = line.rstrip()
        for character in string.punctuation:
            line = line.replace(character,"")
        line = line.lower()
        words = line.split(" ")
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1
    return word_count
        
result = word_counter()
print(result)