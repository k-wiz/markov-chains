from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    opened_file = open(file_path)  

    "This should be a variable that contains your file text as one long string"
    contents = opened_file.read()
    return contents



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
            # Add key to the dictionary.
            chains[key] = [value]
        else:
            # Generate the current value of key (which is a list).
            old_value = chains[key]
            # Append new value to the key list. 
            old_value.append(value)


    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    #Initialize empty string.
    text = ""

    for word_pair in chains:

        #Generate key from dict randomly. 
        words_1_and_2 = choice(chains.keys())
        print "key is: ", words_1_and_2
        #Generate value that corresponds to key; assign it to value_list. 
        value_list = chains.get(words_1_and_2)  
        print "value_list is: ", value_list
        # pick a random value from key list
        word_3 = choice(value_list)
        print "value is: ", word_3

        word_1, word_2 = words_1_and_2

        text = text + word_1 + " " + word_2 + " " + word_3

    print "Text is: ", text

    

    # print text
    # return text


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)
print chains

# Produce random text
random_text = make_text(chains)

print random_text
