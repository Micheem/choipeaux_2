import csv

with open("question14.csv", mode='r', encoding='utf-8') as g:
    reader = csv.DictReader(g, delimiter=',')
    questions = [{key: value for key, value in element.items()} for element in reader]

new_dico = {}


iteme = questions[0].items()


for (cle, valeur) in iteme:
    couple = valeur.split("/")
    dico = {}
    dico[couple[0]] = [int(i) for i in couple[1].split(',')]
    print(dico)
    #new_dico[cle] =

"""
for dico in questions[1:]:
    itemes  = dico.items()
    for item in itemes:
        new_dico[item[0]] += item[1]
"""




"""
new_dico = questions[0]

for dico in questions[1:]:
    itemes  = dico.items()
    for item in itemes:
        new_dico[item[0]] += item[1]

print(new_dico)
"""