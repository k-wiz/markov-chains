from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    opened_file = open(file_path)  

    "This should be a variable that contains your file text as one long string"
    contents = opened_file.read()
    #print contents
    return contents

#contents = open_and_read_file("green-eggs.txt")


def make_chains(text_string):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """
    words = text_string.split()

    chains = {}

    for i in range(len(words) - 2):
        key = (words[i], words[i + 1])
        value = words[i + 2]
        if key not in chains:
            print "im here ############################"
            chains[key] = [value]
            print chains
        else:
            #add i + 2 to the list of values 
            # old_value = chains.get(key) #gives the value
            print key
            old_value = chains[key]
            print "old value", old_value

            chains[key] = old_value.append(value)




    # return chains
    print chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text = ""

    # your code goes here

    return text


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
