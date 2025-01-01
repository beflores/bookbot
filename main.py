def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    # print(f"{num_words} words found in the document")
    count_characters(text, book_path, num_words)



def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_characters(text, path, num_words):
    lower_case = text.lower()
    # return lower_case
    character_counts = {}
    for letter in lower_case:
        if letter.isalpha():
          if letter in character_counts:
              character_counts[letter] += 1
          else:
              character_counts[letter] = 1
    
    # Report

    # Convert dictionary to list of dictionaries
    char_list = []
    for char, num in character_counts.items():
        char_dict = {"char": char, "num": num}
        char_list.append(char_dict)

    # Create sort function
    def sort_on(dict):
        return dict["num"]
    
    # Sort the list
    char_list.sort(reverse=True, key=sort_on)

    print(f"--- Begin report of {path} ---")
    print(f"{num_words} words found in the document")

    for item in char_list:
        print(f"The '{item['char']}' was found {item['num']} times")

    print("--- End report ---")

    return character_counts

main()