import random


for Dé in range(1):
    Dé = [1, 2, 3, 4, 5, 6]
    resultat = random.choice(Dé)
    if resultat == 1:
        print("Face 1.")
    elif resultat == 2:
        print("Face 2.")
    elif resultat == 3:
        print("Face 3.")
    elif resultat == 4:
        print("Face 4.")
    elif resultat == 5:
        print("Face 5.")
    elif resultat == 6:
        print("Face 6.")

while True:
    reponse = input("Voulez-vous rejouer ou vous arrêter ? Tapez \"O\" pour rejouer ou \"N\" pour arrêter.")

    if reponse.upper() == "N":
        print("Partie terminée.")
        exit()
        break
    elif reponse.upper() == "O":
        print("Nouvelle partie.")
        for Dé in range(1):
            Dé = [1, 2, 3, 4, 5, 6]
            resultat = random.choice(Dé)
            if resultat == 1:
                print("Face 1.")
            elif resultat == 2:
                print("Face 2.")
            elif resultat == 3:
                print("Face 3.")
            elif resultat == 4:
                print("Face 4.")
            elif resultat == 5:
                print("Face 5.")
            elif resultat == 6:
                print("Face 6.")

    else:
        print("Veuillez choisir entre \"O\" pour rejouer ou \"N\" pour arrêter.")
