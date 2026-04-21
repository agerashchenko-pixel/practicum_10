def count_vowels_and_consonants(text):
    """
    Count the number of Russian vowels and consonants in the given text.
    :param text: the input string to analyze
    :return: None
    """
    vowels_chars = "аеёиоуыэюя"
    consonants_chars = "бвгджзйклмнпрстфхцчшщ"

    vowels_count = 0
    consonants_count = 0

    for char in text.lower():
        if char in vowels_chars:
            vowels_count += 1
        elif char in consonants_chars:
            consonants_count += 1

    print(vowels_count, consonants_count)


text = input()
count_vowels_and_consonants(text)
