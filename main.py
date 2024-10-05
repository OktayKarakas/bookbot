def main():
    with open("books/frankenstein.txt") as f:
        file_content = f.read()
        print(f"number of words : {count_words(file_content)}")
        count_chars_dict = count_chars(file_content)
        for key in count_chars_dict:
            if key.isalpha():
                print(f"number of {key} occurance : {count_chars_dict[key]}")

def count_words(content):
    words = content.split()
    return len(words)

def count_chars(content):
    chars = {}
    for char in content:
        if not char.lower() in chars:
            chars[char.lower()] = 1
        else:
            chars[char.lower()] += 1
    return chars

main()