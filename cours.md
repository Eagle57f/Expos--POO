# La Programmation Orientée Objet - POO, Partie 1


> ### **Définition:**
>
> La POO est un paradigme de programmation favorisant la structuration du code avec les objets...
> 
> *Le paradigme de programmation est une façon d'approcher la programmation informatique et de formuler les solutions aux problèmes et leur formalisation dans un langage de programmation approprié.*
>
> Concrètement c'est une façon de programmer qui permet de créer et manipuler des objets en créant des classes en python. Vous en croisez partout en python, un entier (int) est un objet, une chaîne de caractère (str) également...
> 
> **Pour comprendre comment ça fonctionne je vous propose un exemple:**
> 
> **Objectif:**
> 
> Créer un objet Soldat possédant un nom, des points de vie (PV), des points d'attaque (ATQ) et des points d'expérience (XP). Il sera capable de manger et d'attaquer un autre soldat.

> ### **Etape 1 - Créer une classe:**
> 
> La création d'une classe permet par la suite de créer plusieurs objets qui auront la même structure. Par convention, un nom de classe commence toujours par une majuscule. Ainsi, voici le début d'une classe:
> 
> ```py
> class Soldat:
>     pass
> ```

> ### **Etape 2 - Les attributs:**
> 
> Les attributs d'une classe forment la structure de celles-ci. Dans mon exemple, les attributs sont comparables au caractéristiques du soldat. Pour créer les attributs, il y'a 2 manières de faire:
> 
> **1) Dans le corps du code:**
> 
> ```py
> class Soldat:
>     pass
> 
> a = Soldat()
> 
> a.atq = 2
> a.nom = 'a'
> ...
> ```
> 
> Dans ce code, je créé un objet de type soldat dans la variable a. On dit que a est une instance de Soldat.
> 
> Ensuite je créé les attributs un par un. Le problème c'est que si je créé un nouvel objet de type soldat, il faut refaire toute la procédure pour lui donner des attributs. Pour contrer cela, il existe la deuxième manière d'opérer:
>
> **2) Avec le constructeur:**
> 
> ```py
> class Soldat:
>     def __init__(self, nom, pv, atq):
>         self.nom = nom
>         self.pv = pv
>         self.atq = atq
>         self.xp = 0
> 
> a = Soldat('a', 20, 5)
> ```
> 
> 
> Dans ce code j'utilise le constructeur (la fonction init) qui permet de créer les attribut directement dans la classe et de leur donner une valeur lors de la création de l'objet. Ainsi, je créé un objet de type Soldat dans la variable a. a est donc une instance de Soldat ayant 'a' pour nom, 20 pv et 5 d'attaque.

> ### **Etape 3 - Les méthodes:**
> 
> Les méthodes d'une classe permettent de faire des opérations avec les objets de la classe. Ces méthodes sont donc des fonctions propres à la classe. Ces fonctions doivent toutes prendre en premier paramètre self qui permet d'appliquer l'opération sur l'objet que l'on cherche à utiliser.
> 
> 
> ```py
> class Soldat:
>     def __init__(self, nom, pv, atq):
>         self.nom = nom
>         self.pv = pv
>         self.atq = atq
>         self.xp = 0
>   
>     def manger(self, combien):
>         self.pv = self.pv + combien
>         print(f'{self.nom} a gagné {combien} pv')
>   
>     def attaquer(self, qui):
>         qui.pv = qui.pv - self.atq
>       print(f'{qui.nom} a perdu {self.atq} pv')
>         self.xp = self.xp + 1
>         print(f'{self.nom} a gagné 1 xp')
> 
> cesar = Soldat('Cesar', 20, 5)
> obelix = Soldat('Obelix', 50, 100)
> 
> print(cesar.atq)
> obelix.manger(5)
> cesar.attaquer(obelix)
> 
> ```
> 
> Ici je créé 2 méthodes:
> 1) manger qui a pour effet de redonner de la vie au soldat. Elle prend en paramètre un entier ou un flottant et ajoute sa valeur aux pv de l'objet.
> 2) attaquer qui permet au soldat d'attaquer un autre soldat. Elle enlève au pv de l'attaqué le montant de l'atq de l'attaquant. Et l'attaquant reçois 1 xp.
> 
> Dans ce dernier code je créé deux objets, cesar et obelix, qui ont chacun des nom, pv, atq et xp différents, mais viennent de la même classe et donc possèdent les mêmes attributs et méthodes.
> 
> On peut print un attribut d'une classe (dans le code, l'atq d'obélix), et la syntaxe d'utilisation de la classe est la suivante: `objet.methode(paramètres...)`. Ainsi Obélix gagne 5 pv en mangeant, mais Cesar les lui reprend tout de suite après en l'attaquant.



> ###  **Ce qu'il faut retenir**
> - Une classe possède des attribut et des méthodes.
> - Une classe permet de générer plusieurs objets du même type.
> 
> Il y'a encore beaucoup de choses possibles avec la POO. Il est aussi intéressant que > la POO est omniprésente en python, puisque tous ce qui est manipulé est objet.