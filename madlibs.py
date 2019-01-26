text = "The [adjective] [noun] jumped over the [noun]."
text_split = text.split(" ")

def read_text(text_split):
    """Returns a list of words to be replaced with user input."""
    parts_of_speech = []
    for word in text_split:
        if word[0] == "[":
            parts_of_speech.append(word[1:-1])
    return parts_of_speech
    

def get_input(read_text):
    """Returns a list of input words from user based on parts of speech in """
    user_input_list = []
    parts_of_speech = read_text(text_split)
    for word in parts_of_speech: 
        input_word = raw_input("Please enter a %s: " % word)
        user_input_list.append(input_word)
    return user_input_list


def make_input_list(get_input):
    user_input_list = get_input(read_text)
    replaced_list = []
    for word in user_input_list:
        replaced_list.append(word)
    return replaced_list


def make_madlib(make_input_list):
    replaced_list = make_input_list(get_input)
    index = 0
    for (i, word) in enumerate(text_split):
        if word[0] == "[":
            text_split[i] = replaced_list[index]
            index += 1
    final_madlibs = " ".join(text_split)        
    print final_madlibs

make_madlib(make_input_list)


