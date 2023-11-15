#function example
def first_part(word):
    for i in word:
        print(i)
first_part("proba")
#if check example
my_list = [1, 2, 3, 4]
if 1 in my_list:
    print('1 is in my list')
if 5 not in my_list:
    print('5 is not in my list')
#while loop example
a=10
while a>=0:
    print(f"a is {a}")
    a-=1
#for loop example
people={"Bob":42,"John":36,"Mitt":115}
for name,age in people.items():
    print("{} is {} years old.".format(name,age))
#range example
for i in range(0,20):
    print(i)
for i in range(10):
    print(i)
for i in range(0,20,3):
    print(i)
for i in range(20,0,-1):
    print(i)
for i in range(20,0,-3):
    print(i)
#match-case example
status=400
match status:
    case 400:
        print("Bad request")
    case 401|403:
        print("Authentication error")
    case 404:
        print("Not found")
    #default value
    case _:
        print("Default alert")
#function with one positional parameter example
def say_hello(name):
    print(f"Hello, {name}")
say_hello("World")
#function with two positional parameters example
def multiply(a,b):
    result=a*b
    print(f"{result}")
multiply(5,6)
#function with one named parameter example
def say_hello_there(name="there"):
    print(f"Hello, {name}")
say_hello_there()
#function with changing count of arguments example
#args holds the positional arguments in a tuple
#kwargs holds the named arguments in a dict(names and values of arguments)
#order is important
def varfunc(some_arg,*args,**kwargs):
    print("args:")
    for i in args:
        print(f"{i}")
    print("kwargs:")
    for i,j in kwargs.items():
        print(f"{i} is {j}")
    print(f"some_arg is {some_arg}")
varfunc("hello",1,2,3,name="Bob", age=42)
#list positions example
nice_things=["coffee","cheese","crackers","tea"]
for nice_thing in nice_things:
    print(f"{nice_thing} is a nice thing")
print(f"fisrt nice thing is {nice_things[0]}")
print(f"last nice thing is {nice_things[-1]}")
print(f"third to last nice thing is {nice_things[-3]}")
#list slicing example
animals=["cat","dog","rabbit","raccoon","panda","red panda","marmot"]
print("domestic animals:")
print(animals[0:3])
print("wild animals:")
print(animals[3:8])
print("animals in reversed order:")
print(animals[::-1])
print("animals in reversed order without the first one:")
print(animals[-1:0:-1])
#list with reference example
tea="coffee","cheese","crackers","tea"
things_i_like=["coffee","cheese","crackers"]
things_you_like=["crackers","coffee",tea]
if things_i_like[0]==things_you_like[1]:
    print("Something in common")
    print(things_you_like[2])
else:
    print("Coffee is not a common interest")
#list strange functionalities example
cheeses=["brie","bergkase","kashkaval","leipajuusto"]
cheeses.append(cheeses)
if cheeses[-1] is cheeses:
    print(cheeses)
else:
    print("not same cheeses")
cheeses=["brie","bergkase","kashkaval","leipajuusto"]
teas=["chai","earl grey","jasmine","oolong"]
breakfast=[cheeses,teas]
print(breakfast)
print(breakfast[0][1])
breakfast[1][2]=["шкембе","люти чушки","оцет с чесън"]
print(teas)
#list methods example
counting=["one","two","three","one","one"]
continuing_counting=["one","two","three","four","five","continuing"]
print(counting.index("one"))
print(counting.count("one"))
counting.append("something")
print(counting)
counting.extend(continuing_counting)
counting.sort()
print(counting)
#tuple strange functionalities example
a,*b,c=1,2,3,4,5
print(a)
print(b)
print(c)