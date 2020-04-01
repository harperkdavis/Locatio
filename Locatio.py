import json, math, random
from staticon import Level, sprint

with open('names.json') as f:
    names = json.load(f)

def generate_name(loc):
    first = names[loc]['firsts'] + names['global']['firsts']
    last = names[loc]['lasts'] + names['global']['lasts']
    location_name = random.choice(first)
    if random.random() < names['lastChance']:
        location_name += random.choice(last)
    return location_name + ' ' + loc


if __name__ == '__main__':
    print(generate_name('ridge').title())
