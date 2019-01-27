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
        if word[0] == "[": # if the first letter of the word is a bracket,
            #add the word, without the brackets, to the output list
            parts_of_speech.append(word[1:-1])
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


# def make_input_list(get_input):
#     """Return a list of input words from user.
    
#     Args:
#         read_text: a function that returns a list of parts of speech.
#     Returns:
#         a list of the words that came from the user's input.

#     """

#     user_input_list = get_input(read_text)
#     replaced_list = []
#     for word in user_input_list:
#         replaced_list.append(word)
#     print replaced_list
#     return replaced_list


def make_madlib(get_input):
    replaced_list = get_input(read_text)
    index = 0
    for (i, word) in enumerate(text_split):
        if word[0] == "[":
            text_split[i] = replaced_list[index]
            index += 1
    final_madlibs = " ".join(text_split)        
    print final_madlibs

make_madlib(get_input)


