import random
print(random.choice(['apple', 'pear', 'banana']))
print(random.sample(range(100), 10)) # sampling tanpa replacement
print(random.random()) # float acak
print(random.randrange(6)) # integer acak yang dipilih dari range(6)