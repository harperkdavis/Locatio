import json, math, random
from staticon import Level, sprint

with open('names.json') as f:
    names = json.load(f)


def generate_name(loc):
    first = names['global']['firsts']
    last = names['global']['lasts']
    if loc in names:
        first += names[loc]['firsts']
        last += names[loc]['lasts']
    location_name = random.choice(first)
    if random.random() < names['lastChance']:
        location_name += random.choice(last)
    if random.random() < names['theChance']:
        location_name = 'the ' + location_name
    if random.random() < names['noPlaceTypeChance']:
        return location_name
    else:
        return location_name + ' ' + loc


if __name__ == '__main__':
    sprint(Level.INFO, generate_name('ridge').title())
    sprint(Level.INFO, generate_name('peak').title())
    sprint(Level.INFO, generate_name('woods').title())
    sprint(Level.INFO, generate_name('base').title())
    sprint(Level.INFO, generate_name('hills').title())
