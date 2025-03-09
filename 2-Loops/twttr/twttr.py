phrase = input("Sentence: ")

no_vowel = "".join([char for char in phrase if char.lower() not in "aeiou"])

print(no_vowel)