# Evaluation of Private Set Intersection. 

import hashlib
import secrets
import sys
import timeit

# Configuration

sys.set_int_max_str_digits(25000000)
iterations = 1000 # `iterations` will benchmark this program a set amount of times.

# Mailboxes, which include data sent by the other party.

r = []
s = []

# Functions

def random_number():
    return secrets.randbits(256) % (10 ** -2) # Temporary workaround for Python's processing overhead.

def H(xi):
    xi = str(xi)
    xi = hashlib.sha256(xi.encode()).hexdigest()
    xi = int(xi, 16)
    return xi

# Program

def execute():

    # Step 1: Receiver (R)

    X = [5, 1, 0]
    a = random_number()
    A = []

    for xi in X:
        ai = H(xi) ** a
        A.append(ai)

    s.append(A)

    # Step 2: Sender (S)

    Y = [2, 7, 0]
    b = random_number();
    B = []
    A_ = []

    for yi in Y:
        bi = H(yi) ** b
        B.append(bi)

    for ai in s[0]:
        ai = ai ** b
        A_.append(ai)

    r.append(B)
    r.append(A_)

    # Step 3: Receiver (R)

    B = []

    for bi in r[0]:
        b_i = bi ** a
        B.append(b_i)

    # Check for Intersection

    intersections = []

    for _hash in B:
        if _hash in r[1]:
            index = r[1].index(_hash)
            intersections.append(X[index])

    if not intersections:
        return None
    else:
        return intersections

if __name__ == '__main__':
    exec_time = timeit.timeit(execute, number=iterations)
    print(f"Completed in {exec_time:.3f} seconds.")
    print(f"Iterations: {iterations}")
