
# Read in the existing concepts
# print all possible combinations of different sizes

# itertools for combinations
from itertools import combinations
from itertools import chain

# json for reading data files
import json

def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s,r) for r in range(len(s)+1))

# read file with concepts
concepts = {}
with open("data.json") as f:
    data = json.load(f)

while True:
    concepts = data["concepts"]
    interactions = data["interactions"]

    interactionSets = map(lambda I: I["related_concepts"], interactions)

    res_set = set(map(tuple, powerset(concepts))) ^ set(map(tuple, interactionSets))
    res_list = list(map(list, res_set))

    for combo in res_list:
        if len(combo) < 2:
            continue

        print(combo)
    
        done = False
        r = ''
        while not done:
            r = input("New interaction: (y/n): ")
            if r == 'y' or r == 'n':
                done = True
        if r == 'y':
            desc = input("Type a description of the interaction: ")
            title = input("Type a title for the interaction: ")
            data["interactions"].append({"related_concepts": combo, "title": title, "description": desc})
            with open("data.json", "w+") as f:
                json.dump(data, f)
    done = False
    r = ''
    while not done:
        r = input("New concept: (y/n): ")
        if r == 'y' or r == 'n':
            done = True
    if r == 'y':
        new_concept = input("Name of concept: ")
        data["concepts"].append(new_concept)
        with open("data.json", "w+") as f:
           json.dump(data, f)
