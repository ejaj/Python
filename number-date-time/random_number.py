import random

values = [1, 2, 3, 4, 5, 6]
# print(random.choice(values))
# print(random.sample(values, 2))
# print(random.sample(values, 2))
# print(random.sample(values, 3))
random.shuffle(values)
print(values)
print(random.randint(0, 10))

# uniform floating-point values
print(random.random())
