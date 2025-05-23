import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
#option 1
print(random.choice(friends))
#option 2
random_friend = random.randint(0, 4)
print(friends[random_friend])