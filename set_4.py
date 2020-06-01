sampleText = "Python is a very powerful language"

vowels = frozenset("aeiou")
finalSet = set(sampleText).difference(vowels)
print(finalSet)

final_list = sorted(finalSet)
print(finalSet)