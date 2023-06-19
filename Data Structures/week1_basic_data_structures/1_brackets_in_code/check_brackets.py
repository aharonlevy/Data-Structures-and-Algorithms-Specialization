# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    text_len = len(text)
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append([i, next])

        if next in ")]}":
            # Process closing bracket, write your code here
            if len(opening_brackets_stack) < 1:
                return i + 1
            elif are_matching(opening_brackets_stack.pop()[1], next):
                continue
            else:
                return i + 1
            pass
    if len(opening_brackets_stack) > 0:
        return opening_brackets_stack.pop()[0] + 1
    return "Success"


def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    print(mismatch)


if __name__ == "__main__":
    main()
