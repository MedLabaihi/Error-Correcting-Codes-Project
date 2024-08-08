import numpy as np
from random import randint

def generate_mot(complexite):
    """
    Generates a random binary word of length `complexite` with at least 2 bits set to 1.
    Ensures that a valid binary word is returned.
    """
    if complexite < 2:
        raise ValueError("Complexity must be at least 2.")

    while True:
        mot = np.random.randint(0, 2, size=complexite)
        if np.sum(mot) >= 2:
            return mot

def ajout_un_binaire(mot):
    """
    Adds 1 to a binary word and returns the next binary word in sequence.
    """
    # Convert binary array to integer, increment, then convert back to binary
    mot_int = int(''.join(map(str, mot)), 2)
    mot_int = (mot_int + 1) % (2 ** len(mot))
    return np.array([int(b) for b in np.binary_repr(mot_int, width=len(mot))])

def calcul_hamming(mot1, mot2):
    """
    Calculates the Hamming distance between two binary arrays.
    """
    return np.sum(mot1 != mot2)

def generate_matrice_aleatoire(ligne, complexite):
    """
    Generates a random parity check matrix with unique rows and each column having at least 2 bits set to 1.
    """
    num_attempts = 0
    while num_attempts < 1000:
        num_attempts += 1
        M = np.array([generate_mot(ligne)])
        while M.shape[0] < complexite:
            mot = generate_mot(ligne)
            if not np.any(np.all(M == mot, axis=1)):
                M = np.vstack([M, mot])
        M = M.T
        if all(np.sum(M, axis=0) >= 2) and M.shape[0] == len(np.unique(M, axis=0)):
            return M
    raise TimeoutError("No valid matrix found after 1000 attempts.")

def verifier_generateur(matrice, nb_bit, complexite):
    """
    Verifies if a matrix is a generator matrix by calculating the minimum Hamming distance between encoded words.
    """
    init = np.zeros((1, nb_bit), dtype=int)
    list_mot = []
    min_ham = float('inf')

    for _ in range(1, 2 ** nb_bit):
        mot_code = np.dot(init, matrice) % 2
        if list_mot:
            distances = [calcul_hamming(mot_code.flatten(), m.flatten()) for m in list_mot]
            min_ham = min(min_ham, *distances)
        list_mot.append(mot_code.flatten())
        init = ajout_un_binaire(init.flatten())

    return min_ham

def generate_matrice_generatrice(ligne, complexite):
    """
    Generates a generator matrix by combining an identity matrix with a random parity check matrix.
    """
    if ligne > complexite ** 2:
        raise ValueError("Number of rows must be less than or equal to the square of the complexity.")

    M = np.eye(ligne, dtype=int)
    G = generate_matrice_aleatoire(ligne, complexite)
    return np.concatenate((M, G), axis=1)

# Example usage
ligne = 4  # Number of bits in unencoded words
complexite = 3  # Number of bits in parity check words

# Generate the generator matrix
M = generate_matrice_generatrice(ligne, complexite)
print("Generator Matrix:\n", M)

# Verify the generator matrix
print("Minimum Hamming Distance:", verifier_generateur(M, ligne, complexite))
