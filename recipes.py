import shelve

blt = ["bacon", "lettuce", "tomato", "bread"]
beans_on_toast = ["beans", "bread"]
eggs = ["eggs", "butter", "milk"]
soup = ["tin of soup"]
pasta =["pasta", "cheese"]

with shelve.open('recipes', writeback=True) as recipes:
    recipes["blt"] = blt
    recipes["beans_on_toast"] = beans_on_toast
    recipes["eggs"] = eggs
    recipes["pasta"] = pasta
    recipes["soup"] =soup

    recipes["blt"].append("butter")

    temp_list = recipes["blt"]
    temp_list.append("butter")
    recipes["blt"] = temp_list

    recipes["soup"].append("croutons")
    recipes["soup"] = soup
    recipes.sync()
    soup.append("cream")

    for snack in recipes:
        print(snack, recipes[snack])

