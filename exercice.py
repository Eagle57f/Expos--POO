import random
import colorama

colorama.init(autoreset=True)


RED = colorama.Fore.RED
BLUE = colorama.Fore.BLUE

class Soldat:
    def __init__(self, hp, dmg):
        self.hp = hp[0]
        self.max_hp = hp[1]
        self.dmg = dmg
    
    def attack(self, ennemy):
        ennemy.hp -= self.dmg
        print(f"{BLUE}Vous avez infligé {RED}{self.dmg} {BLUE}dégats.\rLa vie de l'ennemi est passée de {RED}{ennemy.hp + self.dmg} {BLUE}a {RED}{ennemy.hp} {BLUE}hp")
        if random.randint(0, 3) == 0:
            self.hp -= ennemy.dmg/2
            print(f"{BLUE}L'ennemi a réussi à riposter, il vous inflige {RED}{ennemy.hp/2} {BLUE}dégats.")
        
    def heal_potion(self):
        self.hp += self.max_hp/4

print(f"{BLUE}add nomJoueur")
while True:
    response = input("Commande:  ")
    if response == exit:
        break
    if "add" in response:
        response = response.replace("add ", "")
        print(f"{BLUE}Soldat({colorama.Fore.GREEN}(pv, pv_max){BLUE}, {RED}dégats")
        stats = input("Commande:  ")
        try:
            exec(f"{response} = {stats}")
        except:
            print("Une erreur est survenue")
    else:
        try:
            exec(response)
        except TypeError:
            print(f"{RED}Vous n'avez pas donné assez de paramètres, merci de réessayer.")
        except AttributeError:
            print(f"{RED}Ce Soldat n'exsite pas, ou le Soldat n'a pas cette action.")
        except NameError:
            print(f"{RED}Ce Soldat n'existe pas.")