def plugboard(convertable_text, encoding_pattern):
    pattern_dictionary = dict()
    new_word = ""
    for first_letter, second_letter in encoding_pattern:
        pattern_dictionary[first_letter] = second_letter
        pattern_dictionary[second_letter] = first_letter
    for letter in convertable_text:
        new_word += pattern_dictionary.get(letter, letter)
    return new_word


def rotor(convertable_text, encoding_pattern):
    new_word = ""
    for letter in convertable_text:
        new_word += encoding_pattern.get(letter, " ")
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