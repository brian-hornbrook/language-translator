translations = {
    "hello": "hola",
    "thank you": "gracias",
    "sorry": "lo siento"
}

done = False

while not done:
    print('Type "done" at any time to exit')
    word = input("type a English word to translate to spanish ")
    word.lower()

    if word == "done":
        done = True

    elif word in translations:
        for english, spanish in translations.items():
            if word == english:
                print(english + " is " + spanish + " in spnaish")

    else:
        print("sorry, word isn't in the dictionary")

    print("")
