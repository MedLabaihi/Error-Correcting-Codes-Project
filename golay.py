import numpy as np
from termcolor import colored

# Simule le fonctionnement de la transmission d'un message avec un code correcteur de golay (24,12,8)
# Le programme crée le message à envoyer, génère des erreurs et sépare le message pour identifier les erreurs.

MatGeneratrice = np.array([
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0],
    [1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0],
    [1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1],
    [1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1],
    [1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1],
    [1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0],
    [1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0],
    [1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0],
])

def genererMessage(message):
    """
    Génère le message de 24 bits à envoyer.
    """
    M = np.mod(np.dot(MatGeneratrice, message), 2)
    return M

def messageAlea():
    """
    Génère et renvoie un message de données de 12 bits à transmettre.
    """
    return np.random.randint(2, size=(12, 1))

def afficheMatrice(matrice):
    """
    Permet un affichage propre de matrices colonnes.
    """
    res = np.copy(matrice)
    res.shape = (1, res.shape[0])
    for i in range(matrice.shape[0]):
        print(str(matrice[i]).strip('[]'), " ", end='')
    print()
    return res

def genererErreur(message, s):
    """
    Permet de simuler un nombre s d'erreurs.
    """
    res = np.copy(message)
    for i in range(s):
        b = np.random.randint(len(message))
        res[b] = (res[b] + 1) % 2
    return res

def differenceMatrice(matrice1, matrice2):
    """
    Affichage de différence de 2 matrices, les bits équivalents sont en vert, les différents sont en rouge.
    """
    for i in range(matrice1.shape[0]):
        if matrice1[i] == matrice2[i]:
            print(colored(str(matrice2[i]).strip('[]'), 'green'), " ", end='')
        else:
            print(colored(str(matrice2[i]).strip('[]'), 'red'), " ", end='')
    print()

def partie(message, a):
    """
    Retourne la partie du message comprise entre le bit a et a+12.
    """
    retour = np.zeros((12, 1), dtype=int)
    for k in range(a, a + 12):
        retour[k - a] = message[k]
    return retour

def main():
    # Générer et afficher le message aléatoire de 12 bits
    message = messageAlea()
    print("Data to transmit = ")
    afficheMatrice(message)

    # Générer et afficher le message codé de 24 bits
    encoded_message = genererMessage(message)
    print("Message to send = ")
    afficheMatrice(encoded_message)

    # Nombre d'erreurs à insérer
    num_errors = int(input('Number of errors to insert (integer between 0 and 8): '))
    noisy_message = genererErreur(encoded_message, num_errors)

    print("Received message (with errors) = ")
    afficheMatrice(noisy_message)

    print("Difference display (errors in red) = ")
    differenceMatrice(encoded_message, noisy_message)

if __name__ == "__main__":
    main()
