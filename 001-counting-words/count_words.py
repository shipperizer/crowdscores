import sys


def count_words(lines):
    pass


if __name__ == '__main__':
    stream = sys.stdin
    lines = sys.stdin.readlines()
    for word, count in count_words(lines):
        print word, count
