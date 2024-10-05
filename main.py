def main():
    with open("books/frankenstein.txt") as f:
        file_content = f.read()
        print(f"number of words : {count_words(file_content)}")
        count_chars_dict_list = count_chars(file_content)
        print(count_chars_dict_list)
        for dict in count_chars_dict_list:
            if dict["char"].isalpha():
                print(f"number of {dict['char']} occurance : {dict['num']}")

def count_words(content):
    words = content.split()
    return len(words)

def sort_on(dict):
    return dict["num"]

def count_chars(content):

    chars = {}
    chars_list = []

    for char in content:
        if not char.lower() in chars:
            chars[char.lower()] = 1
        else:
            chars[char.lower()] += 1
        
    for key in chars:
        chars_list.append({"char":key,"num":chars[key]})

    chars_list.sort(reverse=True,key=sort_on)
    return chars_list

main()