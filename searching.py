shopping_list = ["milk", "pasta", "egg","spam", "bread", "rice"]

item_to_find = "spam"
found_at = None

for i in range(len(shopping_list)):
    if shopping_list[i] == item_to_find:
        found_at = i
        break

print("Item found at position {}".format(found_at+1))