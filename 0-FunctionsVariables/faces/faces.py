def convert(str):
    return str.replace(":)","🙂").replace(":(","🙁")

def main():
    emoji = input("What emoji?: ")
    print(convert(emoji))

main()