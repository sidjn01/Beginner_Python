imelda = "More Mayhem", "Imedla May", 2011, (
   [(1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz")]
)
print(imelda)

title, artist, year, track = imelda

print(title)
print(artist)
print(year)

for song in track:
    print("\t", song)
