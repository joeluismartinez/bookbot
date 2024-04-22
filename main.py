

def main():
    letter_dict = dict()
    letter_list = []

    with open("frankenstein.txt") as f:
        file_contents = f.read()

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{len(file_contents.split())} words found in the document\n")
    count_letters(file_contents, letter_dict)
    for item in letter_dict:
        letter_list.append({"name": item, "num": letter_dict[item]})
    letter_list.sort(reverse=True, key=sort_on)
    for item in letter_list:
       print(f"The '{item['name']}' character was found {item['num']} times")
    print("--- End report ---")


def count_letters(file_contents, letter_dict):
    for word in file_contents.split():
        for letter in word:
            key = letter.lower()
            if key not in letter_dict and key.isalpha():
                letter_dict[key] = 0
            if key in letter_dict:
                letter_dict[key] += 1

def sort_on(dict):
    return dict["num"]

main()
