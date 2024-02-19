import json
import argparse
from collections import Counter


def is_anagram(word1, word2):
    return Counter(word1.lower()) == Counter(word2.lower())


def find(query, filename):
    with open(filename, 'r') as file:
        data = json.load(file)
        words = data["words"]["dutch"]
    return {word for word in words if is_anagram(query, word)}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('word', type=str)
    parser.add_argument('-f', '--file', default='words.json')
    args = parser.parse_args()

    anagrams = find(args.word, args.file)
    for anagram in anagrams:
        print(anagram)


if __name__ == "__main__":
    main()
