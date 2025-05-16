from datetime import date
import sys
import inflect
p = inflect.engine()

def main():
	birth_date = date.fromisoformat(input("Date of birth: "))
	todays_date = date.today()
	difference = (todays_date - birth_date).days
	print(p.number_to_words(difference * 24 * 60) + " minutes")

if __name__ == "__main__":
	main()