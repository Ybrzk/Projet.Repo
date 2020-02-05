#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Exercice : Analyser du texte avec Python 
#1. Ecrire une fonction hascap(s) qui renvoie tout les mots de la chaîne
#s commençant par une majuscule.
#Pour ce faire utiliser la fonction ord() pour obtenir le code ASCII des lettres
#(Les lettres majuscule ont un code allant de 65 à 90).


from re import findall


# In[2]:


#Méthode simple pour la 1ère question
s = "Misterheinz Va la bas"
l1 = findall('[A-Z][a-z]+', s)
print(l1)


# In[3]:


s = "Misterheinz Va la bas"
l1 = findall('[A-Z][a-z]+', s)

def hascap(s):
    l1 = s.split() #Créer une liste
    l2 = []
    s1 = s[0]
    s2 = s1
    for i in l1: #Boucle pour chaque i dans la liste ici i sont les mots 
        if ord(i[0]) in range(65, 91): #Condition
            l2.append(i) #Ajoute dans la liste l2
    return l2 #On retourne la l2 
print(hascap(s))


# In[4]:


#2. Proposer une fonction inflation(s) qui va doubler la valeur de tout
# les nombre dans la chaine s. Exemple : « Le prix est de 27 euros »
# devient « Le prix est de 54 euros ».
# Utiliser la fonction enumerate() pour lancer une boucle for (Taper dans
# Google « enumerate boucle for ».)

s1 = "Le prix est de 30 euros"
def inflation(s1):
    l1 = s1.split()
    for i, y in enumerate(l1):
        if y.isnumeric() == True:
            return  int(y)* 2
        
print(inflation(s1))        


# In[5]:


#Proposer une fonction lignes qui à partir d’une long chaîne s (>100
#caractères) renvoie une liste de chaîne de caractères contenant
#chacun 24 caractères maximum et terminant par un espace.
#Voici un exemple de chaîne sur le quel vous pouvez travailler :
#s = "Onze ans déjà que cela passe vite Vous "
#s += "vous étiez servis simplement de vos armes la "
#s += "mort n‘éblouit pas les yeux des partisans Vous «
#s += "aviez vos portraits sur les murs de nos villes«

s = "Onze ans déjà que cela passe vite Vous "
s += "vous étiez servis simplement de vos armes la "
s += "mort n'éblouit pas les yeux des partisans Vous "
s += "aviez vos portraits sur les Murs de nos villes"

def lignes(s): # définition de la fonction lignes
    l1 = [''] # créer une liste vide de chaine de caractére
    l2 = s.split() # mettre la chainede caractére en liste
    for i in l2: # créer une boucle dans l2
        i += " " # on ajoute un espace dans le mots en dérnier 
        if len(l1[-1]) + len(i) <= 24: # si on compte le dérniere élément la liste l1 + la langueur du mot (i)
                                       # inferieur ou égale de 24
            l1[-1] += i # ajouter le mot (i) au dérniere élément à la liste l1
        else: l1.append(i) # si non on ajoute le mot (i) au au dérnier élément de la liste
    return l1 # on fait un retour de l1
print(lignes(s)) # on print la fonction lignes(s)


# In[6]:


#4. Proposer un programme qui renvoie la liste de tout les nombres (y
# compris décimaux et négatifs) d’une chaîne de caractères.
# A tester sur la chaîne : « Les 2 maquereaux valent 6.50 euros ».

from re import findall

s = "Les 2 maquereaux valent 6.50 euros 33 centimes"
def nombre(s):
    l1 = findall('[-]?[0-9][.,,]?[0-9]', s)
    return l1
print(nombre(s))


# In[ ]:




