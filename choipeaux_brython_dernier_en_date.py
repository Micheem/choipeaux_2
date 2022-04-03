from browser import document as doc, html

import csv

doc <= html.H1("Bienvenue sur notre quesionnaire")
doc <= html.IMG(src="choipeaux.png", id="img")

eleve = {'Courage': 10, 'Ambition': 10, 'Intelligence': 10, 'Bontée': 10}

with open("question14.csv", mode='r', encoding='utf-8') as g:
    reader = csv.DictReader(g, delimiter=',')
    questions = [{key: value for key, value in element.items()} for element in reader]

rep = []
i = 0
for _ in questions:
    items = questions[i].items()
    i += 1   
    for (cle, valeur) in items:
        couple = valeur.split("/")
        dico = {}
        dico[couple[0]] = [int(i) for i in couple[1].split(',')]
        rep.append(dico)

reponse = []
nb_qstn = 1
def click(event):
    global nb_qstn
    nb_qstn += 1
    texte = event.target.text
    affichage_question(questions, rep, nb_qstn)
    reponse.append(texte)
    print(reponse)

doc <= html.B('Question', id="texte_qst")
doc <= html.P(html.BUTTON('Reponse', id= "rep1", value=1))
doc <= html.P(html.BUTTON('Reponse', id= "rep2", value=2))
doc <= html.P(html.BUTTON('Reponse', id= "rep3", value=3))

doc['rep1'].bind('click', click)
doc['rep2'].bind('click', click)
doc['rep3'].bind('click', click)



def affichage_question(qstns, r, n_qstn):
    for dico in qstns:   
        dico_qstn = dico
            
    for i in range(n_qstn):
        question = list(dico_qstn.keys())[i]
        rep1 = list(r[i].items())
        rep2 = list(r[11+i].items())
        rep3 = list(r[22+i].items())

    doc["texte_qst"].textContent = question
    doc["rep1"].textContent = rep1[0][0]
    doc["rep2"].textContent = rep2[0][0]
    doc["rep3"].textContent = rep3[0][0]
 

affichage_question(questions, rep, nb_qstn)

