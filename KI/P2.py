import json
import math
import functools

json_file = "fruit.json"

with open(json_file) as json_file:
    json_data = json.load(json_file)
    pairs = json_data.items()
    for key, value in pairs:
        print(key + " " + value)

print("2..................................................................................")


def nfak(n):
    if n <= 0:
        return 1
    return (n * nfak(n - 1))


def create_fak_generator(zahl):
    liste = range(zahl)
    for zahl in liste:
        yield nfak(zahl)


fak_generator = create_fak_generator(14)

for i in fak_generator:
    print(i)

print("3..................................................................................")


def create_drei_up_n_generator(zahl):
    liste = []
    for count in range(zahl):
        liste.append(math.pow(3, count))
    return liste


Drei_up_n_generator = create_drei_up_n_generator(14)

for i in Drei_up_n_generator:
    print(i)

print("4..................................................................................")


def schnitt(liste):
    schnitt = 0.
    for i in liste:
        print(i)
        schnitt += i
    return schnitt / len(liste)


print(schnitt(Drei_up_n_generator))


def schnittl(liste):
    schnittl = functools.reduce(lambda x, y: x + y, liste)
    return schnittl / len(liste)


print(schnittl(Drei_up_n_generator))
