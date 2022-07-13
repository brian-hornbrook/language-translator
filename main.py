import csv

translations = {}

with open("translations.csv", "r") as words:
    reader = csv.DictReader(words, delimiter=",")
    for line in reader:
        english = line["English"].lower()
        spanish = line["Spanish"].lower()
        french = line["French"].lower()
        translations[english] = [spanish, french]

done = False

while not done:
    print('Type "done" at any time to exit')
    word = input("type a English word to translate to spanish ")
    word.lower()

    if word == "done":
        done = True

    elif word in translations:
        for english, translation in translations.items():
            if word == english:
                print(f'{english} is {translation[0]} in spanish and {translation[1]} in french')

    else:
        print("sorry, word isn't in the dictionary")

    print("")
