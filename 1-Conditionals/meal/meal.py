def main():
    time = int(input("Time: ").replace(":", ""))
    if 700 <= time <= 800:
        print("breakfast time" )
    elif 1200 <= time <= 1300:
        print("lunch time")
    elif 1900 <= time <= 2000:
        print("dinner time")
    else:
        print("no meal time")


if __name__ == "__main__":
    main()