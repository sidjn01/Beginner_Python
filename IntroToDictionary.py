fruit = {"orange": "a sweet, orange, citrus fruit",
          "apple": "good for cider"}
# print(fruit)
#
# print(fruit["orange"])
#
# fruit["pear"] = "an odd shaped apple"
# print(fruit)
#
# fruit["pear"] = "great with tequila"
# print(fruit)

# del fruit["pear"]

print(fruit)

# fruit.clear()
# print(fruit["tamato"])
#
# while True:
#     dict = input("Enter a fruit:")
#     if dict == "quit":
#          break
#     # desc = fruit.get(dict, "We don't have a " + dict)
#     # print(desc)
#     if dict in fruit:
#         desc = fruit.get(dict)
#     #     print(desc)
#     else:
#         print("Don't have a " + dict)
#
#
# for snack in fruit:
#     print(fruit[snack])

# for i in range(10):
#     for snack in fruit:
#         print(snack + "is" + fruit[snack])
#     print("*" * 37)
#
# for f in sorted(fruit.keys()):
#     print(fruit[f])

for val in fruit.values():
    print(val)