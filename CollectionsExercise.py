my_favourite_things = ["spam"] * 100
print(my_favourite_things)

#Queue
adjectives=[]

def add_adjective(items):
    adjectives.append(items)

#If pop(0) we get the first inserted element
#If pop() we get the last inserted element
def get_adjective():
    return adjectives.pop(0)

add_adjective("John")
add_adjective("Terry")
add_adjective("Graham")
add_adjective("Eric")

print(", ".join(adjectives) + ", Michael, Terry")

print(get_adjective())
# Joining the values with separator and then .join(our collection)
print(", ".join(adjectives) + ", Michael, Terry")

#Sets
#Unordered unique values

favourite_numbers=set()
favourite_numbers.add(13)
favourite_numbers.add(73)
favourite_numbers.add(32)
favourite_numbers.add(73)
favourite_numbers.add(1024)
favourite_numbers.add(73)

print(favourite_numbers)
print(93 in favourite_numbers)

#We can declare a set with {}, but {} is not an empty set
other_favourite_numbers={32,73,666,13,1024}
print(other_favourite_numbers)

numbers=[1,4,2,6,2,3,6,8,9,3,2,1,5,4,2]
#We can use set() to find the unique values in a list
print(f"Уникалните елементи са: {set(numbers)}")

#Dict
artist_names={
    "John":"Cleese",
    "Terry":"Gilliam",
    "Graham":"Chapman",
    "Eric":"Idle",
}
print("Eric\'s last name is "+artist_names["Eric"])

#{} is an empty dict
#Adding vlues to the dictionary
artist_names["Michael"]="Palin"

#Other ways to create a dictionary
dict(france="Paris",italy="Rome")
dict([("One","I"),("Two","II")])
#Default value "Unknown"
dict.fromkeys([1,2,3],"Unknown")

data = [('John', 'Tilsit'), ('Eric', 'Cheshire'), ('Michael', 'Camembert'),
 ('Terry', 'Gouda'), ('Terry', 'Port Salut'), ('Michael', 'Edam'),
 ('Eric', 'Ilchester'), ('John', 'Fynbo')]
def cheeses_by_owner(cheeses_data):
    by_owner = {}
    for owner, cheese in cheeses_data: # <- tuple unpacking
        if owner in by_owner:
            by_owner[owner].append(cheese)
        else:
            by_owner[owner] = [cheese]
    return by_owner

print(cheeses_by_owner(data))

#List comprehension
#[to do for variable in sequence if condition]
[x*x for x in range(0,10)]
[x*x for x in range(0,10) if x%2]

#One list comprehension can be inserted in another
[(x,y) for x in [1,2,3] for y in [3,1,4] if x!=y]

#Set comprehension
#Same as list comprehension but with {}
import math
{int(math.sqrt(x)) for x in range(1,100)}

#Dict comprehension
{i:chr(65+i) for i in range(10)}

#Deque
from collections import deque
adjectives=deque()
def add_adjective(items):
    adjectives.append(items)
def get_left_adjective():
    return adjectives.popleft()
def get_right_adjective():
    return adjectives.pop()

add_adjective("John")
add_adjective("Terry")
add_adjective("Graham")
add_adjective("Eric")

print(adjectives)
get_left_adjective()
print(adjectives)
get_right_adjective()
print(adjectives)

#Defaultdict
from collections import defaultdict
data = [('John', 'Tilsit'), ('Eric', 'Cheshire'), ('Michael',
'Camembert'),
 ('Terry', 'Gouda'), ('Terry', 'Port Salut'), ('Michael',
'Edam'),
 ('Eric', 'Ilchester'), ('John', 'Fynbo')]
def cheeses_by_owner(cheeses_data):
    by_owner = defaultdict(list)
    for owner, cheese in cheeses_data:
        by_owner[owner].append(cheese)
    return by_owner
print(cheeses_by_owner(data))