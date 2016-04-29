from collections import Counter
import sys
import re

SPECIAL_CHARS = '[\*\.,;]'


def count_words(lines):
    # strip special chars, lowercase and make it a list of words
    lines = re.sub(SPECIAL_CHARS, '', ' '.join(lines)).lower().split()
    # looks like that Counter.most_common gives back a different result sometimes
    # like ('no', 4), ('chin', 2), ('little', 2) or ('no', 4), ('little', 2), ('chin', 2)
    # with a ratio of 3:1 (tried 4 times), so going to sort the result
    words = Counter(lines).most_common()
    # sorting first by lexicographical order, the reverse sorting by number of occurences
    return sorted(sorted(words, key=lambda x: x[0]), key=lambda x: x[1], reverse=True)


if __name__ == '__main__':
    stream = sys.stdin
    lines = sys.stdin.readlines()
    for word, count in count_words(lines):
        print(word, count)
