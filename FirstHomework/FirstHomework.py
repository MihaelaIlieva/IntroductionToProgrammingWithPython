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
        print(begin)
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
        print(begin)
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
        print(begin)
# beginning("шах")
# beginning("Пайтън")
# beginning("Враца")
# beginning("барабани")
# beginning("цици")
# beginning("домашни")
# beginning("se")
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
        print(mid)
    elif len(word)%3==2:
        syllable_length=len(word)//3 #1
        mid=""
        counter=0
        for i in word:
            counter+=1
            if counter>syllable_length+1:
                if counter<=len(word)-syllable_length-1:
                    mid+=i
        print(mid)
    elif len(word)%3==1:
        syllable_length=len(word)//3 #1
        mid=""
        counter=0
        for i in word:
            counter+=1
            if counter>syllable_length:
                if counter<=len(word)-syllable_length:
                    mid+=i
        print(mid)
# middle("шах")
# middle("Пайтън")
# middle("Враца")
# middle("барабани")
# middle("цици")
# middle("домашни")
# middle("se")
def end(word):
    if len(word)%3==0:
        syllable_length=len(word)/3
        fin=""
        counter=0
        for i in word:
            counter+=1
            if counter>len(word)-syllable_length:
                fin+=i
        print(fin)
    elif len(word)%3==2:
        syllable_length=len(word)//3
        fin=""
        counter=0
        for i in word:
            counter+=1
            if counter>len(word)-syllable_length-1:
                fin+=i
        print(fin)
    elif len(word)%3==1:
        syllable_length=len(word)//3
        fin=""
        counter=0
        for i in word:
            counter+=1
            if counter>len(word)-syllable_length:
                fin+=i
        print(fin)
# end("шах")
# end("Пайтън")
# end("Враца")
# end("Барабани")
# end("цици")
# end("домашни")
# end("se")
# def split_sentence(sentence):