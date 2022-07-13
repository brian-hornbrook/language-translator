import csv


def intro():
    print(
        'Welcome to the Spanish and French translator app.\nPlease enter an English word and press the "Enter" key.'
    )
    print('\nType "done" at any time to exit')


def exit():
    print('\nThanks for using the translator app. Have a great day!')


translations = {}

with open("translations.csv", "r") as words:
    reader = csv.DictReader(words, delimiter=",")
    for line in reader:
        english = line["English"].lower()
        spanish = line["Spanish"].lower()
        french = line["French"].lower()
        translations[english] = [spanish, french]

done = False

intro()
while not done:

    word = input("\ntype a English word to translate: ")
    word.lower()

    if word == "done":
        exit()
        done = True

    elif word in translations:
        for english, translation in translations.items():
            if word == english:
                print(f'\nSPANISH: {translation[0]}')
                print(f'\nFRENCH: {translation[1]}')

    else:
        print("\nsorry, word isn't in the dictionary")
