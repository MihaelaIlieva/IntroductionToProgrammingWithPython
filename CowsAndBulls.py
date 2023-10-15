import random

#Digits of number to gues in the game
LENGTH = 4

def get_secret():
    all_digits = list(map(str,range(1,10)))
    random.shuffle(all_digits)
    return "".join(all_digits[:LENGTH])


def compare(our_number,opponents_guess):
    bulls, cows = 0, 0
    for digit_from_our_number, digit_from_opponents_guess in zip(our_number,opponents_guess):
        if digit_from_our_number == digit_from_opponents_guess:
            bulls += 1
        elif digit_from_our_number in opponents_guess:
            cows +=1
    return bulls, cows


OUR_NUMBER=get_secret()
print("Намислих си четирицифрено число без повторение на цифрите и без цифрата нула. Опитай се да познаеш кое е моето число.")
while True:
    opponents_guess = input("Въведи своето предположение:")
    bulls, cows = compare(OUR_NUMBER,opponents_guess)
    if bulls == LENGTH:
        print("Позна!")
        break
    else:
        print(f"Имаш {bulls} бика и {cows} крави.")