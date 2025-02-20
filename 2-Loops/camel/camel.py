def main():
    Phrase = input("Phrase: ")
    print(converter(Phrase))

def converter(sentence):
    snake = ""
    for letter in sentence:
        if letter.isupper():
            snake += "_" + letter.lower()
        else:
            snake += letter
    return snake
main()