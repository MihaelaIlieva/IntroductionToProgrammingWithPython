def plugboard(convertable_text, encoding_pattern):
    pattern_letters = []
    new_word = ""
    for first_letter, second_letter in encoding_pattern:
        pattern_letters.append(first_letter)
        pattern_letters.append(second_letter)
    for letter in convertable_text:
        if letter in pattern_letters:
            if pattern_letters.index(letter)%2 == 0:
                new_word += pattern_letters[pattern_letters.index(letter)+1]
            else:
                new_word += pattern_letters[pattern_letters.index(letter)-1]
        else:
            new_word += letter
    return new_word


def rotor(convertable_text, encoding_pattern):
    new_word = ""
    for letter in convertable_text:
        if letter != " ":
            new_word += encoding_pattern[letter]
        else:
            new_word += " "
    return new_word


def enigma_encrypt(plugboard_position, rotor_position):
    def encryptor(function):
        def encrypt_string(convertable_text):
            return function(rotor(plugboard(convertable_text, 
                                            plugboard_position), 
                                  rotor_position))
        return encrypt_string
    return encryptor


def enigma_decrypt(plugboard_position, rotor_position):
    def decryptor(function):
        def decrypt_string(convertable_text):
            mirror_rotor_pos = dict([(value, key) for key, value in 
                                     rotor_position.items()])
            return function(plugboard(rotor(convertable_text, mirror_rotor_pos), 
                                      plugboard_position))   
        return decrypt_string
    return decryptor