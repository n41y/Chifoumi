from random import*
print("""\n ██████╗██╗  ██╗██╗███████╗ ██████╗ ██╗   ██╗███╗   ███╗██╗
██╔════╝██║  ██║██║██╔════╝██╔═══██╗██║   ██║████╗ ████║██║
██║     ███████║██║█████╗  ██║   ██║██║   ██║██╔████╔██║██║
██║     ██╔══██║██║██╔══╝  ██║   ██║██║   ██║██║╚██╔╝██║██║
╚██████╗██║  ██║██║██║     ╚██████╔╝╚██████╔╝██║ ╚═╝ ██║██║
 ╚═════╝╚═╝  ╚═╝╚═╝╚═╝      ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═╝\n""")
#Presenter le jeu
print("Vous jouez a chifoumi contre l'ordi , il peut choisir 3 options , les voici :\n\n1-Pierre(p)\n2-Feuille(f)\n3-Ciseaux(c)\n")
# Definir ce qui se passera pendant le jeu
def start():
# Demande le choix au joueur
     choix_joueur=str(input("Pierre (p), Feuille (f) ou Ciseaux (c) ?"))
     # Nombre aléatoire entre 1 et 3 car 4 est exclus
     nombreb=randrange(1,4)
# Va donner les rôles au chiffres données
     if nombreb==1 :
        choix_pc="pierre"
     if nombreb==2 :
        choix_pc="feuille"
     if nombreb==3 :
        choix_pc="ciseaux"
# Prevenir l'action de l'ordinateur
     print("L'adversaire a choisi",choix_pc)
# Dire ce qu'il faut faire si le joueur gagne
     def win(a,b) :
        if choix_joueur==a and choix_pc==b :
            print("Tu as gagné")
# Dire ce qu'il faut faire si le joueur perd
     def lose(a,b):
        if choix_joueur==a and choix_pc==b :
            print("L'adversaire a gagné")
# Dire ce qu'il faut faire si il y a égalité
     def egal(a,b):
        if choix_joueur == a and choix_pc == b :
            print("Egalité")
# Tout les cas possibles dans le match :
     win("f","pierre")
     lose("f","ciseaux")
     egal("f","feuille")
     win("p","ciseaux")
     lose("p","feuille")
     egal("p","pierre")
     win("c","feuille")
     lose("c","pierre")
     egal("c","ciseaux")
# Une demande si le joueur veux recommencer uen partie
     retry=str(input("Voulez vous recommencez? YES (y), NO (n)"))
     if retry=="y":
        start()
start()