# https://www.npr.org/2020/03/29/823130995/sunday-puzzle-silent-anagrams
# This week's challenge: Here's an April Foolish puzzle from
# Raymond Nardo of Mineola, N.Y. Think of a world capital.
# Drop the third and fourth letters, and keeping the remaining
# letters in order you'll name a state. What state is it?
import csv
import requests
import pandas
from difflib import get_close_matches

countryCapitals = "https://raw.githubusercontent.com/icyrockcom/country-capitals/master/data/country-list.csv"
# countryCapitals = "https://pkgstore.datahub.io/core/world-cities/world-cities_csv/data/6cc66692f0e82b18216a48443b6b95da/world-cities_csv.csv"
stateNames = "https://raw.githubusercontent.com/jasonong/List-of-US-States/master/states.csv"
csvFile = pandas.read_csv(countryCapitals)
# print(csvFile["capital"])

capitals = []
for cell in csvFile["capital"]:
    toAdd = (cell[:2] + cell[5:]).lower()
    capitals.append(toAdd)

# print (capitals[0])
states = []
csvFile = pandas.read_csv(stateNames)
for cell in csvFile["State"]:
    states.append(cell.lower())

# print(capitals)
# print(states)
for state in states:
    if (len(get_close_matches(state, capitals)) != 0):
        print("---")
        print(state)
        print(get_close_matches(state, capitals))
    # if (get_close_matches(state, capitals)): #capital in states):
        # print(state)
