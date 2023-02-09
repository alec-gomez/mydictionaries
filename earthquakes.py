# open file
import json

infile = open("eq_data.json", "r")

quakes = json.load(infile)
print(type(quakes["features"]))

# 1 Print out number of earthquakes
print(len(quakes["features"]))


# 2/3 iterate though dictionary with mag > 6 (ask teacher how to do with making new dic called eq_dict)
for features in quakes["features"]:
    if features["properties"]["mag"] > 6:
        print(f"location:{features['properties']['place']}")
        print(f"magnitude: {features['properties']['mag']}")
        print(f"longitude: {features['geometry']['coordinates'][0]}")
        print(f"Latitude: {features['geometry']['coordinates'][1]}")
        print()
