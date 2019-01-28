import string

# text = "Every Wednesday, when I get home from school, I have a piano lesson. \
# My teacher is a very strict [noun]. Her name is [female celebrity]. Teacher \
# says I am a natural [noun] and have a good musical [part of the body]. I love \
# piano lessons - they are [adjective]."

# text = "Row, row, row your [noun], [adverb] down the [noun]. Merrily, merrily, \
# merrily, merrily, life is but a [noun]."

text = "The [adjective] [noun] jumped over the [noun]."
  
text_split = text.split(" ")

def read_text(text_split):
    """Return a list of parts of speech.

    Args:
        text_split: a list of words split out from what was originally a string.
    Returns:
        a list of the parts of speech that were in the text_split list. The 
        parts of speech were denoted in text_split by being placed within 
        brackets.

    """

    parts_of_speech = [] # instantiate empty list
    for word in text_split:
        # check if the last index is the other bracket or if it's punctuation
        # this prints the last letter of the prompt correctly
        if word[0] == "[" and word[-1] == "]": 
            parts_of_speech.append(word[1:-1])
        elif word[0] == "[" and word[-1] in string.punctuation: 
            parts_of_speech.append(word[1:-2])
    return parts_of_speech
    

def get_input(read_text):
    """Return a list of input words from user.
    
    Args:
        read_text: a function that returns a list of parts of speech.
    Returns:
        a list of the words that came from the user's input.

    """

    user_input_list = [] # instantiate empty list
    # call the read_text function, and make a variable with its output list
    parts_of_speech = read_text(text_split) 

    for word in parts_of_speech: 
        # for each part of speech, ask user for a word of this type
        input_word = raw_input("Please enter a %s: " % word)
        # add the user's choices to a list
        user_input_list.append(input_word)
    print user_input_list
    return user_input_list


def make_madlib(get_input):
    """Return a final mad lib with parts of speech replaced by user input.
    
    Args:
        get_input: a function that returns a list of words that a user entered.
    Returns:
        a string with the empty parts of speech replaced with a user's chosen
        words.

    """

    # call the get_input function and make a variable from its output list
    replaced_list = get_input(read_text)
    index = 0
    # we want both the index and the word that we want to replace in text_split 
    for (i, word) in enumerate(text_split):
        # find the parts of speech, denoted by brackets
        if word[0] == "[":
            # replace the word at that recorded index with user's input words
            text_split[i] = replaced_list[index]
            # increase index for next loop so that user's next word is used
            index += 1
    final_madlib = " ".join(text_split)        
    print final_madlib

make_madlib(get_input)


