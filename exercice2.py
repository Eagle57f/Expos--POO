
class Personne:
    def __init__(self, name):
        self.name = name

    def marcher(self):
        print(f"{self.name} viens de marcher")

    def parler(self):
        print(f"{self.name} viens de parler")

class Eleve(Personne):
    def __init__(self):
        super().__init__("Eleve")

    def apprendre(self):
        print("Eleve viens d'apprendre")

class Prof(Personne):
    def __init__(self):
        super().__init__("Prof")

    def enseigner(self):
        print("Prof viens d'enseigner")
        
class Cuisinier(Personne):
    def __init__(self):
        super().__init__("Cuisinier")

    def cuisiner(self):
        print("Cuisinier viens de cuisinier")