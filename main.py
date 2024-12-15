def getBookText():
    with open("books/frankenstein.txt") as f:
        text = f.read()
    return text


def count_words():
    text = getBookText()
    words = text.split()
    return len(words)


def count_characters():
    dict = {}
    text = getBookText().lower()
    for char in text:
        if char.isalpha():
            if char in dict:
                dict[char] += 1
            else:
                dict[char] = 1
    return dict


def printer():
    dict_char = dict(sorted(count_characters().items(), key=lambda item: item[0]))
    text = getBookText()
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"The book has {len(text)} characters\n")
    for key, value in dict_char.items():
        print(f"The '{key}' was found {value} times")
    print("--- End of report ---")
printer()