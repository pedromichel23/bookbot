def sort_on(items):
    return items["num"]

def sort_chars_count(chars_count):
    char_count_list = []
    for character in chars_count:
        char = {"char": character, "num": chars_count[character]}
        if character.isalpha():
            char_count_list.append(char)
    return char_count_list


def number_of_words(text):
    words_list = text.split()
    return words_list

def num_chars(words_list):
    chars_count = {}
    for word in words_list:
        for character in word:
            if character.lower() in chars_count:
                chars_count[character.lower()] += 1
            else:
                chars_count[character.lower()] = 1
    return chars_count