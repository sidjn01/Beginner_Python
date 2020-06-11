import pickle
#
# imelda = ("More Mayhem",
#           'Imelda May',
#           '2011',
#           ((1, 'Pulling the rug'),
#            (2, 'Pchyco')))
#
# with open("imelda.pickel", "wb") as pickle_files:
#     pickle.dump(imelda, pickle_files)

with open("imelda.pickel", "rb") as imelda_pickle:
    imelda2 = pickle.load(imelda_pickle)

print(imelda2)

album, artist, year, track = imelda2

print(album)
print(artist)
print(year)

for tracks in track:
    track_num, track_title = track
    print(track_num, track_title)



