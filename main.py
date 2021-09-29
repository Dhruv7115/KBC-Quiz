print('''
---------------------------------------------------------------------------------------------------------------------
                                               Welcome to KBC Quiz
                                                 by Dhruv Bagga
---------------------------------------------------------------------------------------------------------------------
''')

name = input("Enter your name here: ")
choice = input(f'So {name},are you ready for the Quiz: ')
if choice == "yes":
    pass
elif choice == "no":
    exit()

print('''
---------------------------------------------------------------------------------------------------------------------
Q1: In the effort to fight which disease was this slogan used in india: 'Dawai bhi, Kadai bhi? (For 1000 Rupees)
''')
options1 = '''
A: Tuberculosis                                                                B: Polio
C: Dengue                                                                      D: COVID-19
---------------------------------------------------------------------------------------------------------------------
'''
print(options1)
ans1 = input("Enter your ans here: ")

if ans1 == "d":
    print("Your ans is Correct, You won 1000 rupees")

else:
    print("Sorry, you lose")
    exit()

print('''
---------------------------------------------------------------------------------------------------------------------
Q2: The festival of Rakhi falls on which day of the lunar month of shravana? (For 2000 Rupees)
''')
options2 = '''
A: Amavasya                                                                    B: Ashtami
C: Purnima                                                                     D: Ekadashi
---------------------------------------------------------------------------------------------------------------------
'''
print(options2)
ans2 = input("Enter your ans here: ")

if ans2 == "c":
    print("Your ans is Correct, You won 2000 rupees")

else:
    print("Sorry, you lose")
    exit()

print('''
---------------------------------------------------------------------------------------------------------------------
Q3: In mordern times, which of these cities hosted two olympic Games, one in the 19th century and the other in the 21st century? (For 4000 Rupees)
''')
options3 = '''
A: London                                                                    B: Athens
C: Atlanta                                                                   D: Seoul
---------------------------------------------------------------------------------------------------------------------
'''
print(options3)
ans3 = input("Enter your ans here: ")

if ans3 == "b":
    print("Your ans is Correct, You won 4000 rupees")

else:
    print("Sorry, you lose")
    exit()

print('''
---------------------------------------------------------------------------------------------------------------------
Q4: Which of these gods is known as Nandishwara and Chandranath? (For 10000 Rupees)
''')
options4 = '''
A: Lord Shiva                                                                    B: Lord Brahma
C: Lord Indra                                                                   D: Lord Katikeya
---------------------------------------------------------------------------------------------------------------------
'''
print(options4)
ans4 = input("Enter your ans here: ")

if ans4 == "a":
    print("Congratulations, Your all the questions are correct and you won 10000 rupees...")
    exit()

else:
    print("Sorry, you lose")
    exit()