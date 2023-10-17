#This is the refactored code, after the course's team's advice
def beginning(word):
    syllable_length = len(word)//3
    if (len(word)%3 == 0 or len(word)%3 == 1):
        return word[:syllable_length]
    elif len(word)%3 == 2:
        return word[:syllable_length+1]


def middle(word):
    syllable_length = len(word)//3
    if (len(word)%3 == 0 or len(word)%3 == 1):
        return word[syllable_length:len(word)-syllable_length]
    elif len(word)%3 == 2:
        return word[syllable_length+1:len(word)-syllable_length-1]  


def end(word):
    syllable_length = len(word)//3
    if (len(word)%3 == 0 or len(word)%3 == 1):
        return word[len(word)-syllable_length:]
    elif len(word)%3 == 2:
        return word[len(word)-syllable_length-1:] 


def split_sentence(sentence):
    final_list_of_split_words = []
    words = sentence.split()
    for word in words:
        current_tuple = (beginning(word),middle(word),end(word))
        final_list_of_split_words.append(current_tuple)
    return final_list_of_split_words