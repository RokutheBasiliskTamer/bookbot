def main():
    
    run_report("books/frankenstein.txt")

def count_words(text):
    return len(text.split())

def count_chars(text):
    chars_seen = []
    text = text.lower()
    dict_list = []
    for char in text:
        if char.isalpha():
            if char in chars_seen:
                for dictionary in dict_list:
                    if dictionary["char"] == char:
                        dictionary["num"] += 1
            else:
                new_letter = {"char": char,
                              "num": 1}
                dict_list.append(new_letter)
                chars_seen.append(char)

    return dict_list

def sort_on(dict):
    return dict["num"]

def run_report(filename):
    with open(filename) as f:
        file_contents = f.read()
    word_count = count_words(file_contents)
    letter_counts = count_chars(file_contents)
    letter_counts.sort(reverse=True, key=sort_on)
    print(f"--- Begin report of {filename} ---")
    print(f"{word_count} words found in the document")
    for letter in letter_counts:
        print(f"The '{letter["char"]}' character was found {letter["num"]} times")
    print("--- End report ---")
main()