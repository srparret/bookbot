def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    letter_count = get_letter_count(text)
    sorted_letter_list = get_sorted_letter_count(letter_count)

##### Printing the Report!!!!
    print(f"-----Begin report of {book_path}-----")
    print(f"{num_words} words found in the document")
    print()

    for letter in sorted_letter_list:
        if not letter["letter"].isalpha():
            continue
        print(f"The '{letter['letter']}' character was found {letter['num']} times")

    print("-----End Report-----")

    print(f"{num_words} words found in the document")
    print(letter_count)

def get_sorted_letter_count(letter_count):
    sorted_letter_list = []
    for letter in letter_count:
        sorted_letter_list.append({"letter": letter, "num": letter_count[letter]})
    sorted_letter_list.sort(reverse=True, key=sort_on)
    return sorted_letter_list

def sort_on(letter_count):
    return letter_count["num"]

def get_letter_count(text):
    lowered_text = text.lower()
    letter_count={}

    for i in lowered_text:
        letter_count[i] = letter_count.get(i,0) + 1
    return letter_count

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
