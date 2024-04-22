

def main():
    letter_dict = dict()
    with open("frankenstein.txt") as f:
        file_contents = f.read()

    print(file_contents)
    print(len(file_contents.split()))
    count_letters(file_contents, letter_dict)
    print(letter_dict)

def count_letters(file_contents, letter_dict):
    for word in file_contents.split():
        for letter in word:
            if letter not in letter_dict:
                letter_dict[letter.lower()] = 0
            
    return letter_dict

main()
