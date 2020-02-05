#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Exercice Python les classes

#• Ajouter une méthode capsdown() qui passe en minuscule les 
#éléments de la classe « superstring ».

#• Ajouter une méthode tri() qui trie les mots de la classe « superstring »
#par ordre alphabétique. Utiliser les méthodes split(), sorted() et join().

#• Modifier la méthode __str__ de façon à avoir un affichage de la forme
#« type : superstring, content : ECOUTEZ BIEN C'EST TRÈS IMPORTANT
#CE QUE JE DIS ! ».


# In[3]:


class superstring:
    
    def __init__(self, chaîne):
        self.ch = chaîne
    def ajoute(self, char):
        self.ch += char
    def capsdown(self):
        self.ch = self.ch.lower()
    def insert(self, char, i):
        self.ch = self.ch[:i] + char + self.ch[i:]
    def upper(self):
        self.ch = self.ch.upper()
    def __str__(self):
        return self.ch
    def tri(self):
        self.ch


# In[4]:


yacine = superstring("Yacine est un guerrier BERBÈRE")


# In[5]:


yacine.upper()


# In[6]:


print(yacine)


# In[11]:


class superstring :
    def __init__(self, chaine):
        self.ch = chaine
    def tri(self):
        self.ch = self.ch.split(' ')
        self.ch = sorted(self.ch)
        self.ch = ' '.join(self.ch)



    def __str__(self):
        return self.ch

s1 = superstring("ecoutez bien c'est important")
s1.tri()

print(s1)


# In[14]:


class superstring :
    def __init__(self, chaine):
        self.ch = chaine
    def tri(self):
        self.ch = self.ch.split(' ')
        self.ch = sorted(self.ch)
        self.ch = ' '.join(self.ch)
        
    def __str__(self):
        return 'type : superstring, contents: '+self.ch.upper()+'!'


s1 = superstring("ecoutez bien c'est important")
s1.tri()


print(s1)


# In[15]:


#Une classeExercice :
#• Ajouter une méthode qui vérifie si deux formulaires renvoient à la
#même personne.
#• Faire en sorte qu’on puisse afficher les formulaires sous la forme
#[nom, prenom, anneeNaissance]. Créer une liste de formulaire et triez
#la par ordre de naissance. un peut plus élaboré


# In[19]:


#Exemple
class formulaire:
    def __init__(self, nom, prenom, anneeNaissance):
        self.nom = nom.upper()
        self.prenom = prenom.upper()
        self.anneeNaissance = anneeNaissance
    def age(self):
        return 2020 - self.anneeNaissance
    def majeur(self):
        return self.age () >= 18
    def memeFamille(self, formulaire):
        return self.nom == formulaire.nom
    
jd = formulaire ('Yacine', 'Bourezak', 1996)
ad = formulaire ('yacine', "brzk", 1997)

print(jd.majeur())
print(ad.majeur())
print(jd.memeFamille(ad))


# In[31]:


class formulaire:
    
    def __init__(self, nom, prenom, anneeNaissance):
        self.nom = nom.upper()
        self.prenom = prenom.upper()
        self.anneeNaissance = anneeNaissance
    def age(self):
        return 2020 - self.anneeNaissance
    def majeur(self):
        return self.age () >= 18
    def memeFamille(self, formulaire):
        return self.nom == formulaire.nom
    #self est l'objet sur lequel nous travaillons ici "memepersonne"
    def memePersonne(self, formulaire):
        return self.nom == formulaire.nom and self.prenom == formulaire.prenom and self.anneNaissance == formulaire.anneeNaissance
    
jd = formulaire ('Yacine', 'Bourezak', 1996)
ad = formulaire ('yacine', "brzk", 1997)


print(jd.memePersonne(ad))


# In[14]:


class formulaire:
    
    def __init__(self, prenom, nom, anneeNaissance):
        self.nom = nom.upper()
        self.prenom = prenom.upper()
        self.anneeNaissance = anneeNaissance
    def age(self):
        return 2020 - self.anneeNaissance
    def majeur(self):
        return self.age () >= 18
    def memeFamille(self, formulaire):
        return self.nom == formulaire.nom
    #self est l'objet de lui même 
    def memePersonne(self, formulaire):
        return self.nom == formulaire.nom and self.prenom == formulaire.prenom and self.anneNaissance == formulaire.anneeNaissance
    def __str__(self): # def __repr__(self):
        return '('+self.prenom+', '+self.nom+', %s)' % (self.anneeNaissance)
    
yb = formulaire ('Bourezak', 'Yacine', '1996')
hb = formulaire ('Mosbah', 'Hachem', '1983')
lb = formulaire ('Baya', 'Lotfi', '1997')
ip = formulaire ('Makunochi', 'Ippo', '1985')

#print(jd.majeur())
#print(ad.majeur())
#print(jd.memeFamille(ad))
#print(jd, ad)
#rint(ad)

liste_formulaire=[]
liste_formulaire.append(yb)
liste_formulaire.append(hb)
liste_formulaire.append(lb)
liste_formulaire.append(ip)


a = sorted(liste_formulaire, key = lambda year : year.prenom)
# sorted: ordonne la liste formulaire
for i in a:
    print(i)
    

#print(sorted(liste_formulaire, key = lambda year : year.anneeNaissance))


# In[15]:


#Travaille à faire :
#• Créer une fonction plusGrandQue() qui doit faire la comparaison entre
#deux cartes (représenté par des tuples) et donc remplacer la troisième
#partie du code.
#• Créer une fonction piocher() qui doit sélectionner l’ensemble des carte
#tiré par un joueur et donc remplacer la deuxième partie du code .
#• Créer une classe « carte » ayant les attribut couleur et valeur. Elle
#devra être appelé dans la fonction plusGrandQue().


# In[5]:


from random import randrange


# In[6]:


# On initialise toute les couleurs et valeurs que peuvent prendre les cartes 
valeurs = [i for i in range(1, 11)]
couleurs = [i for i in range(1, 5)]
# On choisit le nombre de tour que va durer la partie 
# et on initialise le score à 0
nbTours = 7
score = 0

#Enfin on crée une liste de tuples
#pour présenter le paquet de cartes

paquet = [(v, c) for v in valeurs for c in couleurs]
main1, main2 = [], []


# In[7]:


for i in range(nbTours):
    # Le joueur 1 tire une carte aléatoirement dans le paquet
    x = paquet[randrange(len (paquet))]
    # La carte est ajouté à la main du joueur 1
    main1.append(x)
    # La carte tiré est suprimmé du paquet
    paquet.remove(x)
    # Idem pour le joueur 2
    y = paquet[randrange(len(paquet))]
    main2.append(y)
    paquet.remove(y)


# In[8]:


for i in range(nbTours):
    if main1 [i] [0] > main2 [i] [0] or (
    main1 [i] [0] == main2 [i] [0] and main1 [i] [1] > main2 [i] [1]):
        score += 1
    else:
        score -= 1


# In[9]:


print ("Vainqueur: " + ("joueur 1 " if score > 0 else "joueur 2"))


# In[10]:


def plusGrandQue(carte1, carte2):
    return  carte1 [i] [0] > carte2 [i] [0] or (
    carte1 [i] [0] == carte2 [i] [0] and carte1 [i] [1] > carte2 [i] [1])

for i in range(nbTours):
    if plusGrandQue:
        main1 [i] [0] > main2 [i] [0] or (
        main1 [i] [0] == main2 [i] [0] and main1 [i] [1] > main2 [i] [1])
        score += 1
    else:
        score -= 1
print("Vainqueur: " + ("joueur 1 " if score > 0 else "joueur 2"))


# In[11]:


def pioche(paquet, nbTours):
    main1 = []
    main2 = []
    for i in range(nbTours):
        # Le joueur 1 tire une carte aléatoirement dans le paquet
        x = paquet[randrange(len (paquet))]
        # La carte est ajouté à la main du joueur 1
        main1.append(x)
        # La carte tiré est suprimmé du paquet
        paquet.remove(x)
        # Idem pour le joueur 2
        y = paquet[randrange(len(paquet))]
        main2.append(y)
        paquet.remove(y)
    return main1, main2
a, b = pioche(paquet, 7)
print(a, b)


# In[33]:


print(main1, main2)


# In[29]:


main1[0][0] >= main2[0][0]


# In[13]:


def plusGrandQue(carte1,carte2):  
    return carte1[0]> carte2[0] or (carte1[0] == carte2[0] and carte1[1] > carte2[1])
  
for i in range(nbTours):
    if plusGrandQue(main1, main2):
        score += 1
    else:
        score -= 1        
print("Vainqueur: " , ("joueur 1 " if score > 0 else "joueur 2"))


# In[1]:


from random import randrange

class Card : 
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    def __repr__(self):
        return '('+str(self.value)+',' +str(self.suit)+')'


class Partie :
    def __init__(self, nbvalue, nbsuit, nbround):
        self.nbvalue = nbvalue
        self.nbsuit = nbsuit
        self.nbtour = nbround
    #partie starter doit regroupé le déroulement de la partie
    # def jouer
    def __str__(self):
        return '('+str(self.nbvalue)+','+str(self.nbsuit)+','+str(self.nbround)+')'   

# On initailise toutes les valeurs et couleurs que peuvent prendre les cartes 
valeurs = [i for i in range(1, 11)]
couleurs = [i for i in range(1,5)]

# on choisi le nombre de tour que va durée la partie et on initilise le score à 0

nbTours = 7
score = 0 

# Enfin on crée une liste de tuple pour représenter le paquet de cartes
paquet = [Card(c,v) for v in valeurs for c in couleurs]
main1, main2 = [], []

def pioche(paquet, nbTours):
    for i in range(nbTours):
        # Le joueur 1 tire une carte aléatoirement dans le paquet
        x = paquet[randrange(len(paquet))]
        # La carte est ajouté à la main du joueur 1 
        main1.append(x)
        # La carte est supprimé du paquet
        paquet.remove(x)
        # Idem pour le joueur 2 
        y = paquet[randrange(len(paquet))]
        main2.append(y)
        paquet.remove(y)
    return main1 , main2

main1, main2 = pioche(paquet, nbTours)
    
def plusGrandQue(x,y):
    return x.value > y.value or (x.value == y.value and x.suit > y.suit) 
    
 
for i in range(nbTours):
    if plusGrandQue(main1[i],main2[i]):
        score = 1
    else : 
        score = - 1

print("Vainqueur : " + ("joueur 1"if score > 0 else "joueur 2"))


# In[ ]:




