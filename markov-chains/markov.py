"""Generate Markov text from text files."""
import random
from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    opened_file=open(file_path).read() #opens files as text file
    opened_file=opened_file.replace('\n',' ').split(' ')
    return opened_file
    



def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:    

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """


    chains={}
    new_list=[]

    for i in range(len(input_text)-2):
        pairs=(input_text[i], input_text[i +1]) #starts are first index and moves up one to create tuple 
        third_words=input_text[i+2] #picks the 3rd word 
        if pairs not in chains:
            chains[pairs]=[]
        chains[pairs].append(third_words)

    # print(chains)

    # your code goes here

    return chains


words = []
def make_text(chains):
    """Return text from chains."""
    print(chains)
    keys = ("like", "green") # seed
    words.append(keys[0])
    words.append(keys[1])    
    while True:
        # if there is a key error, stop there
        if keys in chains:
            values = chains[keys]
            word_one= keys[0]
            word_two=keys[1]
            word_three=random.choice(values)
            words.append(word_three)
            keys = (word_two, word_three)
        else:
            break;
    print(' '.join(words))

    return ' '.join(words)


input_path = 'green-eggs.txt'

#Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

#print(random_text)
