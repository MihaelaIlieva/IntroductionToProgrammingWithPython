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