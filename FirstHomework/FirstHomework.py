def beginning(word):
    if len(word)%3==0:
        syllable_length=len(word)/3
        begin=""
        counter=0
        for i in word:
            counter+=1
            if counter>syllable_length:
                break
            else:
                begin+=i
        return(begin)
    elif len(word)%3==2:
        syllable_length=len(word)//3
        begin=""
        counter=0
        for i in word:
            counter+=1
            if counter>syllable_length+1:
                break
            else:
                begin+=i
        return(begin)
    elif len(word)%3==1:
        syllable_length=len(word)//3
        begin=""
        counter=0
        for i in word:
            counter+=1
            if counter>syllable_length:
                break
            else:
                begin+=i
        return(begin)
def middle(word):
    if len(word)%3==0:
        syllable_length=len(word)/3
        mid=""
        counter=0
        for i in word:
            counter+=1
            if counter>syllable_length:
                if counter<=len(word)-syllable_length:
                    mid+=i
        return(mid)
    elif len(word)%3==2:
        syllable_length=len(word)//3
        mid=""
        counter=0
        for i in word:
            counter+=1
            if counter>syllable_length+1:
                if counter<=len(word)-syllable_length-1:
                    mid+=i
        return(mid)
    elif len(word)%3==1:
        syllable_length=len(word)//3
        mid=""
        counter=0
        for i in word:
            counter+=1
            if counter>syllable_length:
                if counter<=len(word)-syllable_length:
                    mid+=i
        return(mid)
def end(word):
    if len(word)%3==0:
        syllable_length=len(word)/3
        fin=""
        counter=0
        for i in word:
            counter+=1
            if counter>len(word)-syllable_length:
                fin+=i
        return(fin)
    elif len(word)%3==2:
        syllable_length=len(word)//3
        fin=""
        counter=0
        for i in word:
            counter+=1
            if counter>len(word)-syllable_length-1:
                fin+=i
        return(fin)
    elif len(word)%3==1:
        syllable_length=len(word)//3
        fin=""
        counter=0
        for i in word:
            counter+=1
            if counter>len(word)-syllable_length:
                fin+=i
        return(fin)
def split_sentence(sentence):
    current_word=""
    final_list_of_split_words=[]
    #the for loop will work only for words that have space after them
    for i in sentence:
        if i !=" ":
            current_word+=i
        else:
            current_tuple=(beginning(current_word),
            middle(current_word),
            end(current_word))
            final_list_of_split_words.append(current_tuple)
            current_word=""
    #getting the last word of the sentence
    index_of_last_space=sentence.rfind(" ")
    last_tupple=(beginning(sentence[index_of_last_space+1:]),
    middle(sentence[index_of_last_space+1:]),
    end(sentence[index_of_last_space+1:]))
    final_list_of_split_words.append(last_tupple)
    return final_list_of_split_words
print(split_sentence("Казвам се Джон Сноу"))