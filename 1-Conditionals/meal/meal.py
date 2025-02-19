def main():
    time = int(input("Time: ").replace(":", ""))
    if 700 <= time <= 800:
        print("breakfast time" )
    elif 1200 <= time <= 1300:
        print("lunch time")
    elif 1800 <= time <= 1900:
        print("dinner time")
    else:
        print("no meal time")


if __name__ == "__main__":
    main()