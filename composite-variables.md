## Dict
if you want to define things inside an entity:

```
player = { "name": "vitor", "age": 18 }
```

## Tuple
if you don't want to define things inside an entity
```
player = ("vitor", 18)
```

## Set
```
male_players = {"vitor", "lucas"}
female_players = {"luana", "vitor"}

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


