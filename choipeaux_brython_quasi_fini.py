from choipeaux_magique_pourlapartie2 import *
from browser import document as doc, html
import csv

doc <= html.H1("Bienvenue sur notre quesionnaire")
doc <= html.IMG(src="choipeaux.png", id="img")

with open("question18.csv", mode='r', encoding='utf-8') as g:
    reader = csv.DictReader(g, delimiter=',')
    questions = [{key: value for key, value in element.items()} for element in reader]

rep = []
i = 0
for _ in questions:
    itemes = questions[i].items()
    i += 1  
    for (cle, valeur) in itemes:
        couple = valeur.split("/")
        dico = {}
        dico[couple[0]] = [int(i) for i in couple[1].split(',')]
        rep.append(dico)

questions[0]['As tu déjà volé un cône de signalisation?'] = rep[0]
questions[0]['As tu peur du vide?'] = rep[1]
questions[0]['Es tu désagréable avec les démarcheurs téléphoniques?'] = rep[2]
questions[0]['As tu un futur ?'] = rep[3]
questions[0]['As tu peur du noir ?'] = rep[4]
questions[0]['La\xa0Terre\xa0est\xa0ronde\xa0?'] = rep[5]
questions[0]['Plus tard tu aimerais avoir un métier?'] = rep[6]
questions[0]['2(2+3)/2'] = rep[7]
questions[0]['La personne dont on ne prononce pas le nom attaque Poudlard que fais tu?'] = rep[8]
questions[0]['Es-tu économe?'] = rep[9]
questions[0]['Un enfant tombe'] = rep[10]

questions[1]['As tu déjà volé un cône de signalisation?'] = rep[11]
questions[1]['As tu peur du vide?'] = rep[1+11]
questions[1]['Es tu désagréable avec les démarcheurs téléphoniques?'] = rep[2+11]
questions[1]['As tu un futur ?'] = rep[3+11]
questions[1]['As tu peur du noir ?'] = rep[4+11]
questions[1]['La\xa0Terre\xa0est\xa0ronde\xa0?'] = rep[5+11]
questions[1]['Plus tard tu aimerais avoir un métier?'] = rep[6+11]
questions[1]['2(2+3)/2'] = rep[7+11]
questions[1]['La personne dont on ne prononce pas le nom attaque Poudlard que fais tu?'] = rep[8+11]
questions[1]['Es-tu économe?'] = rep[9+11]
questions[1]['Un enfant tombe'] = rep[10+11]

questions[2]['As tu déjà volé un cône de signalisation?'] = rep[22]
questions[2]['As tu peur du vide?'] = rep[1+22]
questions[2]['Es tu désagréable avec les démarcheurs téléphoniques?'] = rep[2+22]
questions[2]['As tu un futur ?'] = rep[3+22]
questions[2]['As tu peur du noir ?'] = rep[4+22]
questions[2]['La\xa0Terre\xa0est\xa0ronde\xa0?'] = rep[5+22]
questions[2]['Plus tard tu aimerais avoir un métier?'] = rep[6+22]
questions[2]['2(2+3)/2'] = rep[7+22]
questions[2]['La personne dont on ne prononce pas le nom attaque Poudlard que fais tu?'] = rep[8+22]
questions[2]['Es-tu économe?'] = rep[9+22]
questions[2]['Un enfant tombe'] = rep[10+22]


reponse = []
vrai_rep = []
nb_qstn = 1
nm_qstn = 0 
def click(event):
    global nb_qstn
    global nm_qstn
    if nb_qstn != 10:
        nb_qstn += 1        
        valeur = event.target.value
        affichage_question(questions, rep, nb_qstn)
        reponse.append(questions[int(valeur)])
        rep_provisoire = list(reponse[nm_qstn].values())[nm_qstn].values()
        vrai_rep.append(list(rep_provisoire)[0])

        courage, ambition, intelligence , good  = 0, 0, 0, 0
        for element in vrai_rep:
            courage += element[0]
            ambition += element[1]
            intelligence += element[2]
            good += element[3]
        nm_qstn += 1
        doc['result'].style.display ='none'
    else:
        doc['rep1'].style.display ='none'
        doc['rep2'].style.display ='none'
        doc['rep3'].style.display ='none'
        doc['texte_qst'].style.display ='none'
        doc['result'].style.display ='inline'
        

def resultat(event):
    courage, ambition, intelligence , good  = 0, 0, 0, 0
    for element in vrai_rep:
        courage += element[0]
        ambition += element[1]
        intelligence += element[2]
        good += element[3]
        
    user = {'Courage': 10 + courage , 'Ambition': 10 + ambition, 'Intelligence': 10 + intelligence, 'Good': 10 + good}
    doc <= html.H3(f"La maison attribué à cet élève est {maison(poudlard_characters, user, 7)}")
        
doc <= html.B('Question', id="texte_qst")
doc <= html.P(html.BUTTON('Reponse', id= "rep1", value=0))
doc <= html.P(html.BUTTON('Reponse', id= "rep2", value=1))
doc <= html.P(html.BUTTON('Reponse', id= "rep3", value=2))
doc <= html.H2(html.BUTTON('Résultat', id= "result"))

doc['result'].style.display ='none'
doc['result'].bind('click',resultat)
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