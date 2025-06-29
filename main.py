from stats import number_of_words, num_chars, sort_on, sort_chars_count
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        file_content = f.read()
        return file_content

def print_report(chars_list_dict, file_path, num_words):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for character in chars_list_dict:
        print(f"{character["char"]}: {character["num"]}")
    print("============= END ===============")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        file_path = sys.argv[1]
        book_content = get_book_text(file_path)
        words_list = number_of_words(book_content)
        num_words = len(words_list)
        characters_count = num_chars(words_list)
        chars_list_dict = sort_chars_count(characters_count)
        chars_list_dict.sort(reverse=True, key=sort_on)
        print_report(chars_list_dict, file_path, num_words)


main()