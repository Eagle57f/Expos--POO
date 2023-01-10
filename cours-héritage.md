# La Programmation Orientée Objet - POO, Partie 2


> ### **Définition:**
>
> Maintenant que nous avons vu la base des objets en python, nous allons découvrir l'héritage.
>
> L'héritage est un mécanisme qui nous permet de créer une nouvelle classe – connue sous le nom de classe enfant – qui est basée sur une classe existante – la classe mère, en ajoutant de nouveaux attributs et méthodes en plus de la classe existante. Lorsque vous procédez ainsi, la classe enfant hérite des attributs et méthodes de la classe parent.
> L'héritage est très utile lorsque vous voulez créer des classes similaires.
>
> **Pour comprendre comment ça fonctionne je vous propose un exemple:**
> 
> **Objectif:**
> 
> Créer des objets `Eleve`, `Prof` et `Cuisinier` héritant de l'objet `Personne`, afin de limiter les répétitions de code.
> 
> 

> ### **Problématique:**
> 
> Voici un code avec 3 objets: `Eleve`, `Prof` et `Cuisinier`. Tous peuvent marcher et parler, mais `Eleve` peut apprendre, `Prof` enseigner et `Cuisinier` cuisiner.
> 
> **Problème:** Ce programme est composé majoritairement de répétitions.
> 
> ```py
> class Eleve:
>     def marcher(self):
>         print("Eleve viens de marcher")
> 
>     def parler(self):
>         print("Eleve viens de parler")
> 
>     def apprendre(self):
>         print("Eleve viens d'apprendre")
> 
> class Prof:
>     def marcher(self):
>         print("Prof viens de marcher")
> 
>     def parler(self):
>         print("Prof viens de parler")
>         
>     def enseigner(self):
>         print("Prof viens d'enseigner")
>         
> class Cuisinier:
>     def marcher(self):
>         print("Cuisinier viens de marcher")
> 
>     def parler(self):
>         print("Cuisinier viens de parler")
>         
>     def cuisiner(self):
>         print("Cuisinier viens de cuisinier")
> ```

> ### **Résolution:**
> 
> Nous allons déplacer les méthodes `marcher` et `parler` dans une nouvelle classe: `Personne`, qui va être la classe Parent des objets `Eleve`, `Prof` et `Cuisinier`.
> 
> ```py
> class Personne:
>     def __init__(self, name):
>         self.name = name
> 
>     def marcher(self):
>         print(f"{self.name} viens de marcher")
> 
>     def parler(self):
>         print(f"{self.name} viens de parler")
> 
> class Eleve(Personne):
>     def __init__(self):
>         super().__init__("Eleve")
> 
>     def apprendre(self):
>         print("Eleve viens d'apprendre")
> 
> class Prof(Personne):
>     def __init__(self):
>         super().__init__("Prof")
> 
>     def enseigner(self):
>         print("Prof viens d'enseigner")
>         
> class Cuisinier(Personne):
>     def __init__(self):
>         super().__init__("Cuisinier")
> 
>     def cuisiner(self):
>         print("Cuisinier viens de cuisinier")
> ```
> 
> La ligne `super().__init__()` dans le constructeur sert à appeler les méthodes de la classe parent, et la chaîne de caractère dans `__init__(...)` sert à donner une valeur à la variable `nom` du constructeur de `Personne`.