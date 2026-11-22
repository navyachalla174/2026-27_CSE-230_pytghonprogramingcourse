from functools import reduce

numbers = ____  # e.g. [1, 2, 3, 4, 5]

squares = list(map(lambda x: ____, numbers))
evens = list(filter(lambda x: ____, numbers))
total = reduce(lambda a, b: ____, numbers)

print("Squares:", ____)
print("Evens:", ____)
print("Sum:", ____)