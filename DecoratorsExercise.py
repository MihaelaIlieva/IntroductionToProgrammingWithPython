# Bit operations
def baba():
    print("баница")


def call(function,times):
    for _ in range(times):
        function()

call(baba,4)

#Scopes
# locals() returns dict local variables' names
# globals() returns dict global variables' names
global_one = 1

def foo():
    local_one = 2
    print(locals())

print(globals())
foo()

global_one = 1

def foo():
    global_one = 2
    print(global_one)
    print(locals())

foo()
print(globals())


def outer(x):
    print(x)
    def inner():
        x = 0
        print(x)
    inner()
    print(x)
outer(5)


def start(x):
    def increment(y):
        return x + y
    return increment

first_inc = start(0)
second_inc = start(8)
print(first_inc(3))
print(second_inc(3))
    