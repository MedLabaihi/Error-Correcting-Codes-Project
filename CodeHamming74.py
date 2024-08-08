import numpy as np
from termcolor import colored

def generate_random_message():
    """Generates a random 4-bit message."""
    return np.random.randint(2, size=(4, 1))

def generate_codeword(message):
    """Encodes a 4-bit message into a 7-bit codeword using the generator matrix."""
    G = np.array([[1, 1, 0, 1, 0, 0, 0],
                  [1, 0, 1, 1, 0, 0, 0],
                  [1, 0, 0, 0, 1, 0, 0],
                  [0, 1, 1, 1, 0, 0, 0],
                  [0, 1, 0, 0, 1, 0, 0],
                  [0, 0, 1, 0, 1, 1, 0],
                  [0, 0, 0, 1, 0, 1, 1]])
    return np.mod(np.dot(G, message), 2)

def simulate_errors(codeword, num_errors):
    """Simulates random errors in the codeword."""
    if not (0 <= num_errors <= len(codeword)):
        raise ValueError("Number of errors must be between 0 and 7.")

    result = np.copy(codeword)
    error_positions = np.random.choice(len(codeword), num_errors, replace=False)
    result[error_positions] = (result[error_positions] + 1) % 2
    return result

def detect_error(message):
    """Detects errors in the received message and returns the bit index of the error."""
    H = np.array([[0, 0, 0, 1, 1, 1, 1],
                  [0, 1, 1, 0, 0, 1, 1],
                  [1, 0, 1, 0, 1, 0, 1]])
    syndrome = np.mod(np.dot(H, message), 2)
    if np.all(syndrome == 0):
        return -1
    for i in range(H.shape[1]):
        if np.allclose(syndrome, H[:, i]):
            return i
    return -1

def correct_error(message, bit_index):
    """Corrects the error at the specified bit index."""
    result = np.copy(message)
    result[bit_index] = (result[bit_index] + 1) % 2
    return result

def decode_message(codeword):
    """Decodes the 7-bit codeword into the original 4-bit message."""
    D = np.array([[0, 0, 1, 0, 0, 0, 0],
                  [0, 0, 0, 0, 1, 0, 0],
                  [0, 0, 0, 0, 0, 1, 0],
                  [0, 0, 0, 0, 0, 0, 1]])
    return np.mod(np.dot(D, codeword), 2)

def print_matrix(matrix):
    """Prints the matrix in a readable format."""
    for row in matrix:
        print(" ".join(map(str, row)))

def print_difference(original, modified):
    """Highlights differences between two matrices."""
    for o, m in zip(original, modified):
        for i, (o_bit, m_bit) in enumerate(zip(o, m)):
            color = 'green' if o_bit == m_bit else 'red'
            print(colored(m_bit, color), end=" ")
        print()

def main():
    # Generate and encode message
    C = generate_random_message()
    print("Data to transmit:")
    print_matrix(C.T)

    M = generate_codeword(C)
    print("Message to send:")
    print_matrix(M.T)

    num_errors = int(input('Number of errors to insert (integer between 0 and 7): '))
    K = simulate_errors(M, num_errors)

    print("Received message (with errors):")
    print_matrix(K.T)

    print("Difference (errors in red):")
    print_difference(M.T, K.T)

    error_bit_index = detect_error(K)
    if error_bit_index == -1:
        print("No errors in the received message.")
        L = K
    else:
        print(f"Error detected at bit position: {error_bit_index + 1}")
        L = correct_error(K, error_bit_index)
        print("Corrected message:")
        print_difference(M.T, L.T)

    P = decode_message(L)
    print("Decoded message:")
    print_difference(C.T, P.T)

if __name__ == "__main__":
    main()
