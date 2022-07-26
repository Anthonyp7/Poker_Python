import pandas as pd

def decompose_jeu(tirage):
    dic = {}
    keys = [1,2,3,4,5]
    valeur = []
    couleur = []
    for i,k in zip(tirage,keys):
        dic[k] = i.split('-')
    for key in dic.keys():
        valeur.append(dic[key][0])
        couleur.append(dic[key][1])
    return valeur, couleur

def convert_carte(liste):
    for e,i in zip(liste, range(0,5)):
        try:
            liste[i] = int(e)
        except:
            if e == 'J':
                liste[i] = 11
            elif e == 'Q':
                liste[i] = 12
            elif e == 'K':
                liste[i] = 13
            elif e == 'A':
                liste[i] = 1
            else:
                continue
    return liste

def quinte_flush_royale(tirage):
    valeur_gagnante = ['10','J','Q','K','A']
    valeur, couleur = decompose_jeu(tirage)
    if sorted(valeur_gagnante) == sorted(valeur) and couleur.count(couleur[0]) == 5:
        return True
    else:
        return False

def quinte_flush(tirage):
    valeur, couleur = decompose_jeu(tirage)
    valeur = convert_carte(valeur)
    valeur = sorted(valeur)
    suite = []
    for e, i in zip(valeur[0:-1], range(len(valeur)-1)):
        if e+1 == valeur[i+1]:
            suite.append('True')
    if suite.count('True') == 4 and couleur.count(couleur[0]) == 5:
        return True
    else:
        return False

def carre(tirage):
    valeur, couleur = decompose_jeu(tirage)
    valeur1 = pd.Series(valeur)
    uniques = valeur1.unique()
    count = []
    for i in uniques:
        count.append(valeur.count(i))
    if len(uniques) == 2 and sorted(count) == [1, 4]:
        return True
    else:
        return False

def full(tirage):
    valeur, couleur = decompose_jeu(tirage)
    valeur1 = pd.Series(valeur)
    uniques = valeur1.unique()
    count = []
    for i in uniques:
        count.append(valeur.count(i))
    if len(uniques) == 2 and sorted(count) == [2, 3]:
        return True
    else:
        return False

def flush(tirage):
    valeur, couleur = decompose_jeu(tirage)
    if couleur.count(couleur[0]) == 5:
        return True
    else:
        return False

def quinte(tirage):
    valeur, couleur = decompose_jeu(tirage)
    valeur = convert_carte(valeur)
    valeur = sorted(valeur)
    suite = []
    for e, i in zip(valeur[0:-1], range(len(valeur)-1)):
        if e+1 == valeur[i+1]:
            suite.append('True')
    if suite.count('True') == 4 or valeur == [1, 10, 11, 12, 13]:
        return True
    else:
        return False

def brelan(tirage):
    valeur, couleur = decompose_jeu(tirage)
    valeur1 = pd.Series(valeur)
    uniques = valeur1.unique()
    count = []
    for i in uniques:
        count.append(valeur.count(i))
    if len(uniques) == 3 and sorted(count) == [1, 1, 3]:
        return True
    else:
        return False

def double_paire(tirage):
    valeur, couleur = decompose_jeu(tirage)
    valeur1 = pd.Series(valeur)
    uniques = valeur1.unique()
    count = []
    for i in uniques:
        count.append(valeur.count(i))
    if len(uniques) == 3 and sorted(count) == [1, 2, 2]:
        return True
    else:
        return False

def paire(tirage):
    valeur, couleur = decompose_jeu(tirage)
    valeur1 = pd.Series(valeur)
    uniques = valeur1.unique()
    count = []
    for i in uniques:
        count.append(valeur.count(i))
    if len(uniques) == 4 and sorted(count) == [1, 1, 1, 2]:
        return True
    else:
        return False

def gain(tirage_final, mise):
    if quinte_flush_royale(tirage_final) == True:
        g = mise*250
        resultat = "Quinte Flush Royale!!! Vous gagnez " + str(g) + " euros! Félicitations!!!"
        return g, resultat
    elif quinte_flush(tirage_final) == True:
        g = mise*50
        resultat = "Quinte Flush!!! Vous gagnez " + str(g) + " euros! Félicitations!!!"
        return g, resultat
    elif carre(tirage_final) == True:
        g = mise*25
        resultat = "Carré!!! Vous gagnez " + str(g) + " euros! Félicitations!!!"
        return g, resultat
    elif full(tirage_final) == True:
        g = mise*9
        resultat = "Full!!! Vous gagnez " + str(g) + " euros! Félicitations!!!"
        return g, resultat
    elif flush(tirage_final) == True:
        g = mise*6
        resultat = "Flush!!! Vous gagnez " + str(g) + " euros! Félicitations!!!"
        return g, resultat
    elif quinte(tirage_final) == True:
        g = mise*4
        resultat = "Quinte!!! Vous gagnez " + str(g) + " euros! Félicitations!!!"
        return g, resultat
    elif brelan(tirage_final) == True:
        g = mise*3
        resultat = "Brelan!!! Vous gagnez " + str(g) + " euros! Félicitations!!!"
        return g, resultat
    elif double_paire(tirage_final) == True:
        g = mise*2
        resultat = "Double paire!!! Vous gagnez " + str(g) + " euros! Félicitations!!!"
        return g, resultat
    elif paire(tirage_final) == True:
        g = mise*1
        resultat = "Paire!!! Vous gagnez " + str(g) + " euros! Félicitations!!!"
        return g, resultat
    else:
        g = 0
        resultat = "Perdu! Retentez votre chance :)"
        return g, resultat
