def spam(n):
    spams = ("spam", ) * (n-1)
    return "I would like {} and spam".format(", ".join(spams))


def eggs(n):
    return "I would like {} eggs".format(n)


def served_by(func, server):
    def cached_server(n):
        return "{}, dear {}".format(func(n),server)
    return cached_server

eggs=served_by(eggs, "sir")
spam=served_by(spam, "sir")
print(eggs(10))
print(spam(10))

def thank_you(func):
    def with_thanks(n):
        return "{}. Thank you very much!".format(func(n))
    return with_thanks

eggs=thank_you(served_by(eggs, "sir"))
spam=thank_you(served_by(spam, "sir"))
print(eggs(10))
print(spam(10))

def food(type_of_food, count_of_food):
    return "I would like {} servings of {}".format(count_of_food,type_of_food)
def served_by(function, server):
    def cached_server(type_of_food, count_of_food):
        return "{}, dear {}.".format(function(type_of_food, count_of_food),server)
    return cached_server
def thank_you(function):
    def with_thanks(type_of_food, count_of_food):
        return "{} Thank you very much!".format(function(type_of_food, count_of_food))
    return with_thanks
portion=thank_you(served_by(food,"sir"))
print(portion("eggs", 15))