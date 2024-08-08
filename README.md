# Error-Correcting Codes Project

1. [Overview](#overview)
2. [Mathematical Backgrounds](#mathematical-backgrounds)
3. [Complexity Analysis](#complexity-analysis)
4. [Scripts Description](#scripts-description)
   - [CodeGennarateur](#codegennarateur)
   - [Hamming (8,4) Code Script](#hamming-84-code-script)
   - [CodeCycliqueGeneralises](#codecycliquegeneralises)
   - [CodeHamming(7,4)](#codehamming74)
   - [Golay (24,12,8) Code Script](#golay-24128-code-script)
5. [Contact](#contact)

## Overview
This project explores the application of error-correcting codes, focusing on cyclic codes, Hamming codes, and Golay codes. The project consists of five scripts, each demonstrating different aspects of coding theory, including message generation, encoding, error simulation, and error correction.

## Mathematical Backgrounds

### Cyclic Codes
Cyclic codes are a subclass of linear block codes where if a codeword is cyclically shifted, the result is another codeword. They are defined by their generator polynomial and can be efficiently implemented using shift registers.

### Hamming Codes
Hamming codes are a family of linear error-correcting codes that can detect and correct single-bit errors. The (7,4) Hamming code and (8,4) Hamming code are specific instances where the codeword length is 7 and 8 bits respectively, and the message length is 4 bits.

### Golay Codes
The Golay code is a type of linear error-correcting code that can detect and correct up to 3 errors in a 24-bit codeword. The (24,12,8) Golay code has a codeword length of 24 bits, a message length of 12 bits, and a minimum Hamming distance of 8.

## Complexity Analysis
- **Encoding Complexity**: Encoding a message using generator matrices involves matrix multiplication, which has a complexity of O(n*m) for an n-bit message and an m-bit codeword.
- **Error Detection and Correction**: The complexity depends on the number of parity-check equations and the method used for error correction. For example, detecting errors in Hamming codes is O(n) for the parity-check and O(1) for single-bit error correction.
- **Error Simulation**: Introducing errors involves selecting positions randomly, which has a complexity of O(e), where e is the number of errors.

## Description of Each Program

### [Cyclic Codes Script](./CodeCycliqueGeneralises.py)

This script demonstrates the implementation of cyclic codes. It includes functions for:
- Converting arrays to polynomial string representations.
- Performing circular shifts on arrays.
- Comparing matrices for equality.
- Generating circular permutations of an array.
- Encoding messages using a generator matrix.

### [Hamming (7,4) Code Script](./CodeHamming74.py)

This script handles the Hamming (7,4) code and includes functions for:
- Generating random 4-bit messages.
- Encoding these messages into 7-bit codewords.
- Simulating errors in the codewords.
- Detecting and correcting errors in received messages.
- Decoding the 7-bit codewords back into 4-bit messages.

### [CodeGennarateur](./CodeGenerateur.py)

The `CodeGennarateur` script is designed to demonstrate encoding and error correction using a custom generator matrix. Key features of this script include:
- **Message Generation**: It generates a random 12-bit message to be encoded.
- **Encoding**: Utilizes a generator matrix to transform the 12-bit message into a 24-bit codeword.
- **Error Simulation**: Allows for the introduction of errors into the codeword to simulate transmission errors.
- **Error Detection and Correction**: Identifies and corrects errors by comparing the received codeword with the original encoded message.
- **Matrix Display**: Provides a clean output of the message, codeword, and any errors introduced or corrected.

This script is useful for understanding how different generator matrices affect the encoding process and how errors can be handled in practice.

### [Hamming (8,4) Code Script](./CodeHamming84.py)

The `CodeHamming84` script focuses on encoding and decoding using the (8,4) Hamming code. It features:
- **Message Encoding**: Converts a 4-bit message into an 8-bit codeword using the Hamming (8,4) generator matrix.
- **Error Simulation**: Introduces a specified number of random errors into the codeword to simulate real-world data corruption.
- **Error Detection and Correction**: Detects and corrects errors using the parity-check matrix associated with the (8,4) Hamming code. It provides functionality to identify the erroneous bit and correct it.
- **Decoding**: Transforms the corrected 8-bit codeword back into the original 4-bit message.
- **Matrix Visualization**: Includes functions to display matrices and highlight differences between the original and received messages.

This script is essential for understanding the practical application of Hamming codes in error detection and correction, illustrating how these codes can ensure data integrity in communication systems.

### [Golay Code Script](./GolayCode.py)

This script simulates the use of Golay (24,12,8) codes for encoding and decoding messages. It includes functions for:
- Generating messages.
- Simulating errors.
- Displaying differences between the original and received messages.
- Correcting errors and decoding the messages.

## Contact  
For any questions or feedback regarding this project, please contact:

- **Name**: Labaihi Mohammed
- **Email**: [m.labaihi@gmail.com]
- **GitHub**: [Labaihi Mohammed](https://github.com/MedLabaihi)

Feel free to contribute to this project or reach out for further discussions on coding theory and its applications.

