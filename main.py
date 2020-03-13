from Wikirator.wikirator import Wikirator

test = Wikirator('Wikirator/countries.json', 'result')
for item in test:
    print(item)