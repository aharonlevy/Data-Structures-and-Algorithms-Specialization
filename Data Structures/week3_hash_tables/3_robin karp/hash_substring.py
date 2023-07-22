# python3
import random


def read_input():
    return (input().rstrip(), input().rstrip())


def print_occurrences(output):
    print(" ".join(map(str, output)))


def pre_hashing(text, pattern_length, prime, x):
    text_length = len(text)
    hash_array = [0] * (text_length - pattern_length + 1)
    # create a string of the last pattern_length - 1 letters
    _string = text[(text_length - pattern_length) :]
    hash_array[-1] = poly_hash(_string, prime, x)

    # calculate x^pattern_length
    y = 1
    for _ in range(pattern_length):
        y = (y * x) % prime

    # calculate the hash of every substring and save in hash_array
    for i in reversed(range(text_length - pattern_length)):
        hash_array[i] = (
            (x * hash_array[i + 1]) + ord(text[i]) - (y * ord(text[i + pattern_length]))
        ) % prime
    return hash_array


def poly_hash(target_string, prime, x):
    target_string_hash = 0
    string_length = len(target_string)

    # Calculate the hash using polynomial rolling hash
    for i in reversed(range(string_length)):
        target_string_hash = (target_string_hash * x) + ord(target_string[i])
    return target_string_hash % prime


def rabin_karp(pattern, text):
    prime = (len(text) * len(pattern)) + 2
    x = random.randint(1, (prime - 1))
    positions = []
    pattern_hash = poly_hash(pattern, prime, x)
    text_hash_array = pre_hashing(text, len(pattern), prime, x)

    # Iterate through the text to find pattern occurrences
    for i in range(len(text) - len(pattern) + 1):
        if pattern_hash != text_hash_array[i]:
            continue
        if pattern == text[i : i + len(pattern)]:
            positions.append(i)
    return positions


if __name__ == "__main__":
    print_occurrences(rabin_karp(*read_input()))
