# Performance Evaluation for ED25519, and SECP256R1.

import ecdsa
from ecdsa import ellipticcurve
import timeit

# Options

"""
In this evaluation, there are two selectable options:
    -> SECP256R1 [ecdsa.curves.NIST256p]
    -> ED25519    [ecdsa.curves.Ed25519] | X25519 and Ed25519 are both based on Curve25519.
"""

# Configuration

iterations = 1000 # `iterations` will benchmark this program a set amount of times.
curve = ecdsa.curves.Ed25519
evaluation_type = "addition" # The evaluation type can either be 'addition', or 'multiplication'.

# Program

def evaluate():
    G = curve.generator

    for _ in range(iterations):
        if evaluation_type != "addition" and evaluation_type != "multiplication":
            return "An evaluation type must be specified."
        
        if evaluation_type == "addition":
            P = G + G
        elif evaluation_type == "multiplication":
            # This returns an integer based on a random array of bytes.
            k = int.from_bytes(ecdsa.util.random(32), byteorder="big") # Scalar, P = G(k).
            P = k * G

            
                                     
if __name__ == '__main__':
    exec_time = timeit.timeit(evaluate, number=iterations)
    print(f"Completed in {exec_time:.6f} seconds.")
    print(f"Iterations: {iterations}")
