import re
import sys
from collections import deque


def is_palindrome(phrase: str):
    phrase = re.sub(r'\s+', '', phrase.lower())
    symbols = deque(phrase)
    match = True
    while len(symbols) > 1 and match:
        match = match and symbols.pop() == symbols.popleft()
    return match


def main():
    words = sys.argv[1:]
    if len(words) == 0:
        print(f'Please, provide a phrase')
        return
    phrase = ' '.join(words)
    if is_palindrome(phrase):
        print(f'Palindrome: `{phrase}`')
    else:
        print(f'Not a palindrome: `{phrase}`')


if __name__ == '__main__':
    main()
