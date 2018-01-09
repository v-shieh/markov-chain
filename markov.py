"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    with open(file_path) as text:
        text_str = text.read()

    return text_str


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}
    word_lst = text_string.split()
    bigrams = []

    # for i in range(len(word_lst) - 1):
    #     bigrams.append((word_lst[i], word_lst[i+1]))

    # for i in range(len(bigrams) - 1):
    #     # curr_tuple = (word_lst[i], word_lst[i+1])
    #     if bigrams[i] in chains:
    #         values_lst = chains[bigrams[i]]
    #         values_lst.append(bigrams[i + 1][1])
    #         chains[bigrams[i]] = values_lst
    #     else:
    #         chains[bigrams[i]] = [bigrams[i + 1][1]]

    for i in range(len(word_lst) - 2):
        curr_tuple = (word_lst[i], word_lst[i+1])
        
        if curr_tuple in chains:
            values_lst = chains[curr_tuple]
            values_lst.append(word_lst[i + 2])
            chains[curr_tuple] = values_lst
        else:
            chains[curr_tuple] = [word_lst[i + 2]]
      
    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    chosen_key = choice(chains.keys())
    chosen_value = choice(chains[chosen_key])

    words.append(chosen_key[0])

    while True:
        try:
            chosen_key = (chosen_key[1], chosen_value)
            chosen_value = choice(chains[chosen_key])
            words.append(chosen_key[0])
        except KeyError:
            words.append("I am.")
            break

    return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
