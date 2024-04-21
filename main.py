

def main():

    with open("frankenstein.txt") as f:
        file_contents = f.read()

    print(file_contents)
    print(len(file_contents.split()))
    count_letters(file_contents)


def count_letters(file_contents):
    for word in file_contents.split():
        for letter in word:
            print(letter)



main()
