
Eval1 = []
n = 0

def ajoutNotes(n,tab):
    while True:
        n = int(input("Entrez la note sur 20 : "))
        if n >= 0 or n <= 20:
            tab.append(n)
            break
        else:
            print("Erreur : la note doit être comprise entre 0 et 20. Réessayez.")
    return tab

nbr = int(input("Combien de note ?"))

for k in range (nbr):
    ajoutNotes(n,Eval1)

for j in range (nbr):
    print("-note " + str(j + 1) + ": " + str(Eval1[j]) )





