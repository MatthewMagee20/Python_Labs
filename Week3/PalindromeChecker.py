def EnterPhrase():

    phrase = input("\nEnter phrase: ").lower()

    if Check(phrase):
        print("\nPhrase/Word is a palindrome!")

    else:
        print("\nPhrase/Word is not palindrome")

    print("\n******************************************")


def RemPunctuation(text1):

    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~ '''

    no_punct = ""

    for char in text1:
        if char not in punctuations:
            no_punct = no_punct + char

    return no_punct


def Check(text):

    text = RemPunctuation(text)

    textRev = text[::-1]

    return text == textRev


print("------ PALINDROME CHECKER PROGRAM ------")
print("\n******************************************")

EnterPhrase()
