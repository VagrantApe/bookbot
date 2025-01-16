import string
def word_split(text):
    return text.split()

def word_count(text):
    return len(list(text))

def char_count(word):
    return len(word.lower().split())

def main():
    alphabet = list(string.ascii_lowercase)
    letters_dict = {}
    file_contents = None
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()

    words = word_split(file_contents)
    for w in words:
        chars = w.lower().split()
        for c in list(chars)[0]:
            if c in alphabet:
                if c in letters_dict:
                    letters_dict[c] += 1
                else:
                    letters_dict[c] = 1

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count(words)} words found in the document")
    for char in letters_dict:
        print(f"The '{char}' characer was found {letters_dict[char]} times")
    print("--- End report ---")
main()


