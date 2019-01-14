def search4vowels(phrase: str) -> set:
    """Find and return all vowels in provided phrase"""
    return search4letters(phrase)


def search4letters(phrase: str, what_to_search: str = 'aeiou') -> set:
    """Find and return all provided data in provided phrase"""
    return set(what_to_search).intersection(set(phrase))
