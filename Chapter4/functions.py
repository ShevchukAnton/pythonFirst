"""Find all vowels in provided words"""


def search4vowels(word):
    vowels = set('aeiou')
    found = vowels.intersection(set(word))
    for vowel in found:
        print(vowel)
