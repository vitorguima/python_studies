# Composed variables
## Dict
if you want to define things inside an entity:

```
player = { "name": "vitor", "age": 18 }
player.pop('key_to_remove')
player['new_key_to_add'] = value
```

## Tuple
if you don't want to define things inside an entity
```
player = ("vitor", 18)
``` 

## Set
A collection of unique and non ordered elements. Allows to implement operations like intersection, difference and union.

```
male_players = {"vitor", "lucas"}
female_players = {"luana", "vitor"}
set = set()

male_players.intersection(female_players) = {"vitor"}
male_players.difference(female_players) = {"lucas", "luana"}
male_players.union(female_players) = {"lucas", "luana", "vitor"}
```

## List
```
player = ["vitor", "age"]
```

## Set vs Lists and Tuples
Lists and tuples are standard Python data types that store values in a sequence. Sets are another standard Python data type that also store values. The major difference is that sets, unlike lists or tuples, cannot have multiple occurrences of the same element and store unordered values.

## Frozenset
Alternative form of set but immutable. It's elements cannot be changed during the execution of the program.


# Conditional structures    

```
if salary <= 2000:
    position = "estagiário"
elif 2000 < salary <= 5800:
    position = "júnior"
elif 5800 < salary <= 7500:
    position = "pleno"
elif 7500 < salary <= 10500:
    position = "senior"
else:
    position = "líder"
```

#Iteration
```
a = ['Vitor', 'Ana', 'Bruno', 'Pink', 'Floyd']
```

# Repetition structures

## for loop

```
restaurants = [
    {"name": "Restaurante A", "nota": 4.5},
    {"name": "Restaurante B", "nota": 3.0},
    {"name": "Restaurante C", "nota": 4.2},
    {"name": "Restaurante D", "nota": 2.3},
]

filtered_restaurants = []
min_rating = 3.5

Differente ways to create a new list based on some criteria:

for restaurant in restaurants:
    if restaurant["nota"] > min_rating:
        filtered_restaurants.append(restaurant)
print(filtered_restaurants)

List comprehension
min_rating = 3.0
filtered_restaurants = [restaurant
                         for restaurant in restaurants
                         if restaurant["nota"] > min_rating]
print(filtered_restaurants)  

print list withou B and D characteres
nomes = ['Duda', 'Rafa', 'Cris', 'Yuri']
nomes2 = [s for s in nomes if 'a' in s]
print(nomes2)

Output
['Duda', 'Rafa']
```

## while loop

```
n = 10
last, next = 0, 1
while last < n:
    print(last)
    last, next = next, last + next
```

## enumerate

```
languages = ['Python', 'Java', 'JavaScript']

enumerate_prime = enumerate(languages)

# create items into a tuple
print(list(enumerate_prime))

# output: [(0, 'Python'), (1, 'Java'), (2, 'JavaScript')]
```


