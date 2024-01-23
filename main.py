def main():
    book_path = "bookbot/books/frankenstein.txt"
    book_text = get_book_text(book_path)
    word_count = get_word_count(book_text)
    letter_counts = get_letter_counts(book_text)
    get_report(book_path, word_count, letter_counts)

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def get_word_count(text):
    words = text.split()
    return len(words)

def get_letter_counts(text):
    letter_counts = {}
    for letter in text:
        letter = letter.lower()
        letter_counts[letter] = letter_counts.get(letter, 0) + 1
    return letter_counts

def get_report(book_path, word_count, letter_counts):
    intro_line = f"--- Begin report of {book_path} ---\n"
    word_count_line = f"{word_count} words were found in the document\n\n"
    closing_line = "--- End report ---"
    char_counts_text = ""
    char_counts_list = letter_counts.items()

    char_counts_list = sorted(char_counts_list)
    for char_count in char_counts_list:
        char = char_count[0]
        count = char_count[1]
        if char.isalpha():
            char_counts_text += f"The '{char}' character was found {count} times\n"

    
    report = intro_line + word_count_line + char_counts_text + closing_line 
    print(report)



            

if __name__ == "__main__":
    main()