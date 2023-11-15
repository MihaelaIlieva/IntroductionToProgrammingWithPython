from typing import Any


class Spam:
    def __call__(self):
        print("It works!")

print(type(Spam))
Spam()()

class Statue:
    def __init__(self):
        self.left_hand = 'Generic left hand'
        self.right_hand = 'Generic right hand'
venus_de_milo = Statue()
print(f"I have {venus_de_milo.left_hand} and {venus_de_milo.right_hand}")
del venus_de_milo.left_hand
#print(venus_de_milo.left_hand)

class Hand:
    def __init__(self):
        self.thumb = "Палец"
        self.index_finger = "Показалец"
        self.middle_finger = "Среден"
        self.ring_finger = "Безименен"
        self.pinkie = "Кутре"
    def __getitem__(self,index):
        return (self.thumb, self.index_finger, self.middle_finger,self.ring_finger,self.pinkie)[index]
    def __setitem__(self,index,value):
        if index == 0:
            self.thumb = value
        elif index == 1:
            self.index_finger = value
        elif index == 2:
            self.middle_finger = value
        elif index == 3:
            self.index_finger = value
        elif index == 4:
            self.pinkie = value
    def __getattr__(self, name):
        return f"Това е ръка v1.0. Все още няма {name} :("
    def __setattr__(self, name, value):
        print (f"Нова стойност за {name} - {value}")
        object.__setattr__(self,name,value)
    def __getattribute__(self, name):
        print(f"Някой ми бърка по пръстите и иска {name}")
        return object.__getattribute__(self,name)
hand = Hand()
print(hand.middle_finger)
print(hand[4])
hand[1] = "кебапче"
print(hand[1])
print(hand.sixth_finger)
hand.pinkie = "Малък пръст"


class Limb:
    name = "Limb"
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"I am a {self.name}"
    
class Hand(Limb):
    name = "Hand"
    def introduce(self):
        return f"I am THE {self.name}"

hand=Hand("Герсим")
print(hand.introduce())


class Инженер:
    def introduce(self):
        return "инж."
class Академик:
    def introduce(self):
        return "акад."
class Професор:
    def introduce(self):
        return "проф."
class Сульо(Професор, Академик, Инженер):
    pass
сульо = Сульо()
print(сульо.introduce()) # ?