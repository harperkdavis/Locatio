import json, math, random
from staticon import Level, sprint

with open('names.json') as f:
    names = json.load(f)

def generateName(category):
    firsts = names['global']['firsts']
    lasts = names['global']['lasts']
    if category in names:
        firsts += names[category]['firsts']
        lasts += names[category]['lasts']

    if random.random() < names['config']['commonNameChance']:
        locationName = random.choice(names['names'])
    else:
        locationName = random.choice(firsts)

    if random.random() < names['config']['lastChance']:
        locationName += f' {random.choice(lasts)}'
    if random.random() < names['config']['theChance']:
        locationName = f'the {locationName}'
    if random.random() < names['config']['placeTypeChance']:
        locationName += f' {category}'

    return locationName.title()

if __name__ == '__main__':
    sprint(Level.INFO, generateName('ridge'))
    sprint(Level.INFO, generateName('peak'))
    sprint(Level.INFO, generateName('woods'))
    sprint(Level.INFO, generateName('base'))
    sprint(Level.INFO, generateName('hills'))
