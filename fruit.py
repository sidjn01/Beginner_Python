fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}

veg = {"cabbage": "every child's favourite",
       "sprout": "mmmmm, lovely"}

veg.update(fruit)

print(veg)
a = fruit.copy()
