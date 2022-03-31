from browser import document as doc, html
from choipeaux_magique_pourlapartie2 import *
import csv

doc <= html.H1("Bienvenue sur notre quesionnaire")
doc <= html.IMG(src="choipeaux.png", id="img")

eleve = {'Courage': 10, 'Ambition': 10, 'Intelligence': 10, 'Bontée': 10}


with open("question7.csv", mode='r', encoding='utf-8') as g:
    reader = csv.DictReader(g, delimiter=',')
    questions = [{key: value for key, value in element.items()} for element in reader]

for dico in questions:
    for keys in ['Courage', 'Ambition', 'Intelligence', 'Good']:
        dico[keys] = list(dico[keys])

questions.split(' ')
print(questions)    

nb_qstn = 1
def click(event):
    reponse = []
    global nb_qstn
    nb_qstn += 1
    affichage_question(questions, nb_qstn)
    texte = event.target.text
    print(texte)
    reponse.append(texte)


doc <= html.B('Question', id="texte_qst")
doc <= html.P(html.BUTTON('Reponse', id= "rep1"))
doc <= html.P(html.BUTTON('Reponse', id= "rep2"))
doc <= html.P(html.BUTTON('Reponse', id= "rep3"))
doc['rep1'].bind('click', click)
doc['rep2'].bind('click', click)
doc['rep3'].bind('click', click)

def affichage_question(qstn, nm_qstn):

    for dico in qstn:
        if int(dico['n_qstn']) == nm_qstn:
            dico_qstn = dico
            break
    
    question = dico_qstn['QUESTIONS']
    rep1 = dico_qstn['Réponse 1']
    rep2 = dico_qstn['Réponse 2']
    rep3 = dico_qstn['Réponse 3']
    good = dico_qstn['Good']
    ambition = dico_qstn['Ambition']
    intelligence = dico_qstn['Intelligence']
    courage = dico_qstn['Courage']

    doc["texte_qst"].textContent = question
    doc["rep1"].textContent = rep1
    doc["rep2"].textContent = rep2
    doc["rep3"].textContent = rep3


affichage_question(questions, nb_qstn) 



