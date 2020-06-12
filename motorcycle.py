import shelve

with shelve.open('bike') as bike:
    bike["make"] = "honda"
    bike["model"] = "250 dream"
    bike["colour"] = "red"
    bike["engine"] = 250

    print(bike["engine"])
    print(bike["model"])