"""
------------------
Problem Statement: 
Given N iterables combine them as follows
------------------
------------
SAMPLE_INPUT

sample_1 = [10, 20]
sample_2 = [30, 40]
------------
SAMPLE_OUTPUT

[(10,30), (20,40)]
------------
SAMPLE_INPUT

sample_1 = [10, 20]
sample_2 = [30, 40, 50]
------------
SAMPLE_OUTPUT

[(10,30), (20,40), ('FILLVALUE', 50)]

"""

from itertools import zip_longest
players = ['Ronaldo','Messi', 'Mbappe']
country = ['Portugal','Argentina','France', 'India']
goals = [819, 790, 228]

# takes in iterable and returns an iterator of tuples scenario 1
output = set(zip(players, country, goals))
print(output)


# takes in iterable and returns an iterator of tuples scenario 2 works on Python>=3.10
output = set(zip(players, country, goals, strict=True))
print(output)


# takes in iterable and returns an iterator of tuples scenario 3
output = set(zip_longest(players, country, goals, fillvalue='?'))
print(output)
