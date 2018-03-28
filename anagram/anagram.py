from collections import defaultdict
import time

def parse_dictionary(filename):
    word_anagrams = defaultdict(list)

    with open(filename) as dictionary:
        for word in dictionary:
            word = word.rstrip()
            word_anagrams[''.join(sorted(word))] = [word]

    return word_anagrams

def parse_lookup_words(filename):
    words_lookup = []

    with open(filename) as lookup_words:
        for word in lookup_words:
            word = word.rstrip()
            words_lookup.append(word)

    return words_lookup

def main():
    start_time = time.time()
    word_anagrams = parse_dictionary("vocabulary.txt")
    words_lookup = parse_lookup_words("test_words.txt")

    for word in words_lookup:
        sorted_word = ''.join(sorted(word))

        if word_anagrams[sorted_word]:
            word_anagrams[sorted_word].append(word)
    for words in sorted(word_anagrams.values()):
        if len(words) > 1:
            print(', '.join(words))

    end_time = time.time()
    print(end_time - start_time)

if __name__ == "__main__":
    main()
