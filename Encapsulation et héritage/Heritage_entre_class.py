#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 1. Créer une class data qui hérite du formulaire et possède un attribut supplémentaire id.
# Une méthode doit permettre d’initialiser cette identifiant comme
# une combinaison de caractères pris dans chaque autre attribut.


# In[11]:


class formulaire:
    def __init__(self, nom, prenom, naissance):
        self.nom = str(nom).upper()
        self.prenom = str(prenom).upper()
        self.naissance = naissance
    def _set_naissance(self, naissance):
        na = str(naissance)
        if na.isnumeric():
            self._naissance = int(na)
        else:
            self._naissance = 1900
    def _get_naissance(self):        
        print("Année de naissance :" , self._naissance)
        return   self._naissance 
    naissance = property(_get_naissance, _set_naissance)
    def age(self):
        return 2020 - self._naissance
    def majeur(self):
        return self.age() >= 18
    def memeFamille(self, formulaire):
        return self.nom == fromulaire.nom
    
#class fille

class data(formulaire):
    def __init__(self, nom, prenom, naissance):
            formulaire.__init__(self, nom, prenom, naissance)
    def buildID(self):
        self.id = self.nom[:2] + self.prenom[:2] + str(self.age())
        
jd = data('Yacine', 'Data', 1996)
ad = data ('Mohamed', 'Data', 1988)
jd.buildID()
ad.buildID()
print(jd.id)
print(ad.id)


# In[12]:


# 2. Recensement est une classe qui prend pour entrée 3 listes de formulaire
# et qui à pour méthode permanents() qui retourne la liste des individus
# présent dans ces 3 listes.
# Créer une class listeelectorale qui hérite de recensement et possède une
# méthode renvoyant tout les formulaires présent dans les trois listes et
# correspondants à des personnes majeurs.


# In[13]:


class formulaire:
    def __init__(self, nom, prenom, naissance):
        self.nom = str(nom).upper()
        self.prenom = str(prenom).upper()
        self.naissance = naissance
    def _set_naissance(self, naissance):
        if str(type(naissance)) == "<class 'list'>":
            naissance = ''.join(naissance)
        if str(type(naissance)) == "<class 'str'>" and naissance.isnumeric():
            naissance = int(naissance)
        if str(type(naissance)) == "<class 'int'>":
            self._naissance = naissance
        #else:
        #    self._naissance = 1900
    def _get_naissance(self):        
        return   self._naissance 
    naissance = property(_get_naissance, _set_naissance)
    def _set_nom(self, nom):
        if str(type(nom)) == "<class 'str'>":
            nom = str(nom)
            self._nom = nom
    def _get_nom(self):
        return   self._nom 
    nom = property(_get_nom, _set_nom)
    def _set_prenom(self, prenom):
        if str(type(prenom)) == "<class 'str'>":
            prenom = str(prenom)
            self._prenom = prenom
    def _get_prenom(self):
        return   self._prenom
    prenom = property(_get_prenom, _set_prenom)
    def age(self):
        return 2020 - self._naissance
    def majeur(self):
        return self.age() >= 18
    def memeFamille(self, formulaire):
        return self.nom == fromulaire.nom
    def __str__(self):
        s = self.nom + ", " + self.prenom + ", "
        return s+ str(self.naissance)
    
class recensement:
    def __init__(self, l1, l2, l3):
        self.f2020 = l3
        self.f2019 = l2
        self.f2018 = l1
    def permanents(self):
        return [f for f in self.f2020 if f in self.f2019 and self.f2018]
class listelectorale(recensement):
    def __init__(self, l1, l2, l3):
        recensement.__init__(self, l1, l2, l3)
    def inscrits(self):
        return [f for f in self.permanents() if f.majeur()]

    
jd = formulaire('Doe', 'John', 1987)
ad = formulaire('doe', 'Alice', 1996)
ma = formulaire('Mouhammed', 'Ali', 2004)
cc = formulaire('Coco', 'Chanel', 2001)

l = listelectorale([jd, ad, cc],[jd, ad, ma, cc], [ad, ma, cc])
for f in l.inscrits():
    print(f)


# In[ ]:




