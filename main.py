def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = len(text.split())
    characters = {}
    for char in text:
        c = char.lower()
        if c in characters:
            characters[c] += 1
        else:
            characters[c] = 1
    char_list = list(characters.items())
    char_list.sort(key=lambda x: x[1], reverse=True)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words} words found in the document")
    print("")
    for c in char_list:
        if c[0].isalpha():
            print(f"The {c[0]} character was found {c[1]} times")
    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()