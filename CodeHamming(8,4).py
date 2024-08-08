import numpy as np
from termcolor import colored

def generate_random_message():
    """
    Generates and returns a random 4-bit message.
    """
    return np.random.randint(2, size=(4, 1))


def encode_message(message):
    """
    Encodes a 4-bit message into an 8-bit codeword using the (8,4) Hamming code generator matrix.
    """
    G = np.array([[1, 1, 0, 1], [1, 0, 1, 1], [1, 0, 0, 0], [0, 1, 1, 1],
                  [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1], [1, 1, 1, 0]])
    return np.mod(np.dot(G, message), 2)


def simulate_errors(message, num_errors):
    """
    Simulates the introduction of `num_errors` errors into the 8-bit message.
    """
    if not (0 <= num_errors <= 8):
        raise ValueError("Number of errors must be between 0 and 8.")

    result = np.copy(message)
    error_indices = np.random.choice(len(message), num_errors, replace=False)
    result[error_indices] = (result[error_indices] + 1) % 2
    return result


def detect_error(message):
    """
    Detects and locates errors in the message using the parity check matrix.
    Returns the index of the erroneous bit or -1 if no error is found,
    -2 if there is an even number of errors, or a random index for an odd number of errors.
    """
    H = np.array([[0, 0, 0, 1, 1, 1, 1, 0],
                  [0, 1, 1, 0, 0, 1, 1, 0],
                  [1, 0, 1, 0, 1, 0, 1, 0]])
    syndrome = np.mod(np.dot(H, message), 2)

    if np.all(syndrome == 0):
        return -1  # No error detected

    if parity_check(message) != message[7]:
        for i in range(H.shape[1]):
            if np.array_equal(syndrome, H[:, i]):
                return i  # Return the index of the erroneous bit
    else:
        return -2  # Even number of errors detected


def parity_check(message):
    """
    Computes the parity of the message excluding the parity bit.
    """
    return np.sum(message[:-1]) % 2


def correct_error(message, index):
    """
    Corrects an error by flipping the bit at the specified index.
    """
    corrected = np.copy(message)
    corrected[index] = (corrected[index] + 1) % 2
    return corrected


def decode_message(message):
    """
    Decodes an 8-bit codeword into the original 4-bit message using the (8,4) Hamming code decoding matrix.
    """
    D = np.array([[0, 0, 1, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 1, 0, 0, 0],
                  [0, 0, 0, 0, 0, 1, 0, 0],
                  [0, 0, 0, 0, 0, 0, 1, 0]])
    return np.mod(np.dot(D, message), 2)


def display_matrix_difference(matrix1, matrix2):
    """
    Displays the differences between two matrices. Matching bits are shown in green, differing bits in red.
    """
    for i in range(matrix1.shape[0]):
        if np.array_equal(matrix1[i], matrix2[i]):
            print(colored(''.join(map(str, matrix2[i].astype(int))), 'green'), " ", end='')
        else:
            print(colored(''.join(map(str, matrix2[i].astype(int))), 'red'), " ", end='')
    print()


def display_matrix(matrix):
    """
    Displays a matrix in a readable column format.
    """
    matrix = np.copy(matrix).reshape((1, matrix.shape[0]))
    for row in matrix:
        print(' '.join(map(str, row.astype(int))), " ", end='')
    print()
    return matrix


def display_parity_check_result(matrix, bit_index):
    """
    Displays the parity check matrix with the error bit highlighted.
    """
    print(" 1 2 3 4 5 6 7 8")
    print(" --------------------")
    for i in range(matrix.shape[0]):
        print('| ', end='')
        for j in range(matrix.shape[1]):
            if j == bit_index:
                print(colored(matrix[i, j], 'green'), " ", end='')
            else:
                print(matrix[i, j], " ", end='')
        print('|')
    print(" --------------------")


def main():
    message = generate_random_message()
    print("Data to transmit = ")
    display_matrix(message)

    encoded_message = encode_message(message)
    print("Message to send = ")
    display_matrix(encoded_message)

    num_errors = int(input('Number of errors to insert (integer between 0 and 8): '))
    noisy_message = simulate_errors(encoded_message, num_errors)

    print("Received message (with errors) = ")
    display_matrix(noisy_message)

    print("Difference display (errors in red) = ")
    display_matrix_difference(encoded_message, noisy_message)

    error_index = detect_error(noisy_message)
    if error_index == -1:
        print("No errors detected in the received message.")
        corrected_message = noisy_message
    elif error_index == -2:
        print("Even number of errors detected. Message cannot be decoded, please resend.")
        corrected_message = None
    else:
        print(f"Error detected at bit = {error_index + 1}")
        corrected_message = correct_error(noisy_message, error_index)
        print("Corrected message = ")
        display_matrix_difference(encoded_message, corrected_message)

    if corrected_message is not None:
        decoded_message = decode_message(corrected_message)
        print("Decoded message = ")
        display_matrix_difference(message, decoded_message)

        display_parity_check_result(np.array([[0, 0, 0, 1, 1, 1, 1, 0],
                                              [0, 1, 1, 0, 0, 1, 1, 0],
                                              [1, 0, 1, 0, 1, 0, 1, 0]]), error_index)


if __name__ == "__main__":
    main()
