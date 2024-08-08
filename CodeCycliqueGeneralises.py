import numpy as np

def ArraytoPolynomial(array):
    """
    Converts an array of coefficients to a polynomial string representation.
    """
    terms = []
    size = len(array)
    for i in range(size):
        if array[i] == 1:
            if i == 0:
                terms.append("1")
            elif i == 1:
                terms.append("x")
            else:
                terms.append(f"x^{i}")
    return " + ".join(terms) if terms else "0"

def shifting(array):
    """
    Performs a circular shift on the array.
    """
    return np.roll(array, 1)

def comparerMatrice(array1, array2):
    """
    Compares two arrays (matrices) for equality.
    """
    return np.array_equal(array1, array2)

def permutations(array):
    """
    Generates all unique circular permutations of an array.
    """
    generator = []
    perm = array
    seen = set()
    while tuple(perm) not in seen:
        generator.append(perm)
        seen.add(tuple(perm))
        perm = shifting(perm)
    return np.array(generator)

def permutationsmin(array):
    """
    Generates a few (up to 3) circular permutations of an array.
    """
    generator = []
    perm = array
    i = 0
    while tuple(perm) not in generator and i < 3:
        generator.append(perm)
        perm = shifting(perm)
        i += 1
    return np.array(generator)

def codage(mot, generator):
    """
    Encodes a message using a generator matrix.
    """
    code = (np.dot(mot, generator)) % 2
    return code

if __name__ == "__main__":
    motGenerateur = np.array([1, 1, 0, 1, 0, 0, 0])
    mot = np.array([1, 1, 1, 0])

    generator = permutationsmin(motGenerateur)
    code = codage(mot, generator)
    print('Mot codé : ', code)
    print('Polynomial: ', ArraytoPolynomial(motGenerateur))
