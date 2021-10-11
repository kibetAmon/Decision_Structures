"""
a program that does a search in a text file
  containing names and ages
    by: amon
"""

'''
search_name function that:
   that prints lines where name starts with letter "A"
  '''


def search_name():
    infile = open("names.txt", "r")
    first_letter = input("Enter the search letter: ")
    for s in infile:
        if s[0].lower() == first_letter.lower():
            print(s)


# search_age function prints lines where ages are equal to 5
def search_age():
    infile = open("names.txt", "r")
    for s in infile:
        name_age = s.split()
        if int(name_age[1]) == 5:
            print(s)


def search_name_1(d):
    infile = open("names.txt", "r")
    for s in infile:
        if s[0] == d:
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


'''
Extra:
 Allowing the user to choose display age from the choices available
'''


def search_age_2():
    infile = open("names.txt", "r")
    choice = int(input(" 1.Display age equal to:\n"
                       " 2.Display age less or equal to:\n"
                       " 3.Display age greater or equal to:\n Enter your choice from the above: "))
    age = int(input("Enter the display age: "))
    for s in infile:
        name_age = s.split()
        age_1 = int(name_age[1])
        if choice == 1:
            if age == age_1:  # ages equal to user's input
                print(s)
        elif choice == 2:
            if age >= age_1:  # ages less or equal to user's input
                print(s)
        elif choice == 3:
            if age <= age_1:  # ages greater or equal to user's input
                print(s)


main()
search_age_2()
