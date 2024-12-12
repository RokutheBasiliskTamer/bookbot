def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print(count_words(file_contents))
    print(count_chars(file_contents))

def count_words(text):
    return len(text.split())

def count_chars(text):
    chars_seen = {}
    text = text.lower()
    for char in text:
        if char.isalpha():
            if char in chars_seen:
                chars_seen[char] += 1
            else:
                chars_seen[char] = 1
    return chars_seen

main()