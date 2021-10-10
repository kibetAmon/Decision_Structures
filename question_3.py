#a program that does a search in a text file
  # containing names and ages

def search_name():
    infile = open("names.txt", "r")
    first_letter = input("Enter the search letter: ")
    for s in infile:
        if s[0].lower() == first_letter.lower():
            print(s)


def search_age():
    infile = open("names.txt", "r")
    age = input("Enter the search age: ")
    for s in infile:
        name_age = s.split()
        if int(name_age[1]) == int(age):
            print(s)


def search_name_1(d):
    infile = open("names.txt", "r")
    for s in infile:
        if (s[0] == d):
            print(s)


def search_age_1(age):
    infile = open("names.txt", "r")
    for s in infile:
        if age in s:
            print(s)


def main():
    print("""
        1. Search by name
        2. Search by age 
        """
          )
    ans = int(input("What will you want to do? "))
    if ans == 1:
        s = (str(input("Enter the first letter: ")).upper())
        search_name_1(s)

    elif ans == 2:
        age = str(input("Enter the age: "))
        search_age_1(age)
    else:
        print("Invalid choice, Try again")


main()


