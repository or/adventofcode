#!/usr/bin/python3
import sys

def is_valid(password):
    good = False
    for i in range(len(password) - 2):
        if ord(password[i]) == ord(password[i + 1]) - 1 == ord(password[i + 2]) - 2:
            good = True
            break

    if not good:
        return False

    good = False
    first = None
    for i in range(len(password) - 1):
        if password[i] != first and password[i] == password[i + 1]:
            if not first:
                first = password[i]
            else:
                good = True
                break

    if not good:
        return False

    return True

def next_password(password):
    index = len(password) - 1
    while True:
        if index < 0:
            password = 'a' + password
            break

        jump = False
        c = password[index]
        if c == 'z':
            next_char = 'a'
        else:
            next_char = chr(ord(c) + 1)
            if next_char in 'iol':
                next_char = chr(ord(next_char) + 1)
                jump = True

        if jump:
            password = password[:index] + next_char + 'a' * len(password[index + 1:])
        else:
            password = password[:index] + next_char + password[index + 1:]

        if next_char == 'a':
            index -= 1
            continue

        break

    return password


def next_valid_password(password):
    password = next_password(password)
    while not is_valid(password):
        password = next_password(password)

    return password

password = next_valid_password("hxbxwxba")
print(password)
print(next_valid_password(password))
