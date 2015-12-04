#!/usr/bin/python3
from hashlib import md5

def find_solution(secret, zeroes):
    i = 0
    while True:
        s = (secret + str(i)).encode('ascii')
        hash = md5(s).hexdigest()
        if hash.startswith('0' * zeroes):
            return i

        i += 1

print(find_solution('bgvyzdsv', 5))
print(find_solution('bgvyzdsv', 6))

