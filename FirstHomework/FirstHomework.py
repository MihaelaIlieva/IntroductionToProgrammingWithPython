# In the process of solving the homework, I rewrote the code in fewer lines
# For the first three functions it is comented
# For the fourth one, the shorter version is the working one
# The original one is comented 
def beginning(word):
    begin = ""
    counter = 0
    syllable_length = len(word)//3
    if len(word)%3 == 0:
        for letter in word:
            counter += 1
            if counter <= syllable_length:
                begin += letter
    elif len(word)%3 == 2:
        for letter in word:
            counter += 1
            if counter <= syllable_length+1:
                begin += letter
    elif len(word)%3 == 1:
        for letter in word:
            counter += 1
            if counter <= syllable_length:
                begin += letter
    return begin
    # for letter in word:
    #     counter+=1
    #     if (((len(word)%3 == 0 or len(word)%3 == 1) and 
    #     counter <= syllable_length) or 
    #     (len(word)%3 == 2 and counter <= syllable_length+1)):
    #         begin += letter
    # return begin


def middle(word):
    mid = ""
    counter = 0
    syllable_length = len(word)//3
    if len(word)%3 == 0:
        for letter in word:
            counter += 1
            if counter > syllable_length:
                if counter <= len(word)-syllable_length:
                    mid += letter
    elif len(word)%3 == 2:
        for letter in word:
            counter += 1
            if counter > syllable_length+1:
                if counter <= len(word)-syllable_length-1:
                    mid += letter
    elif len(word)%3 == 1:
        for letter in word:
            counter += 1
            if counter > syllable_length:
                if counter <= len(word)-syllable_length:
                    mid += letter
    return mid
    # for letter in word:
    #     counter+=1
    #     if (((len(word)%3 == 0 or len(word)%3 == 1) and 
    #     counter > syllable_length and 
    #     counter <= len(word)-syllable_length) or 
    #     (len(word)%3 == 2 and 
    #     counter > syllable_length+1 and 
    #     counter <= len(word)-syllable_length-1)):
    #         mid += letter
    # return mid    


def end(word):
    fin = ""
    counter = 0
    syllable_length = len(word)//3
    if len(word)%3 == 0:
        for letter in word:
            counter += 1
            if counter > len(word)-syllable_length:
                fin += letter
    elif len(word)%3 == 2:
        for letter in word:
            counter += 1
            if counter > len(word)-syllable_length-1:
                fin += letter
    elif len(word)%3 == 1:
        for letter in word:
            counter += 1
            if counter > len(word)-syllable_length:
                fin += letter
    return fin
    # for letter in word:
    #     counter += 1
    #     if (((len(word)%3 == 0 or len(word)%3 == 1) and
    #     counter > len(word)-syllable_length) or
    #     (len(word)%3 == 2 and 
    #     counter > len(word)-syllable_length-1)):
    #         fin += letter
    # return fin    


def split_sentence(sentence):
    #Before finding the split function
    # current_word = ""
    # final_list_of_split_words = []
    # #The for loop will work only for words that have space after them
    # for i in sentence:
    #     if i != " ":
    #         current_word += i
    #     else:
    #         current_tuple = (beginning(current_word),
    #         middle(current_word),
    #         end(current_word))
    #         final_list_of_split_words.append(current_tuple)
    #         current_word = ""
    # #Getting the last word of the sentence
    # index_of_last_space = sentence.rfind(" ")
    # #in case the sentence ends with space
    # if sentence[index_of_last_space+1:] != "":
    #     last_tupple = (beginning(sentence[index_of_last_space+1:]),
    #                  middle(sentence[index_of_last_space+1:]),
    #                  end(sentence[index_of_last_space+1:]))
    #     final_list_of_split_words.append(last_tupple)
    # return final_list_of_split_words

    #Optimising with the split function
    final_list_of_split_words = []
    words = sentence.split()
    for word in words:
        current_tuple = (beginning(word),middle(word),end(word))
        final_list_of_split_words.append(current_tuple)
    return final_list_of_split_words