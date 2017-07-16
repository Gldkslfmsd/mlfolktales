import os
import fnmatch


def animal():
    vokabelbuch = {}

    path = "../../../../Fairytale Corpus/English/"

    sonderzeichen = ['.', ',', '"', '?', '-', '!', "'", ':', ';', '—', '[', ']']

    clone = path

    Animal = ["Anecdotes and Jokes/Jokes about Clergymen and Religious Figures",
              "Anecdotes and Jokes/Stories about a Fool",
              "Anecdotes and Jokes/Stories about a Man",
              "Anecdotes and Jokes/Stories about a Woman",
              "Anecdotes and Jokes/Stories about Married Couples",
              "Anecdotes and Jokes/Tall Tales"]

    pathlist = [Animal]

    for element in pathlist:

        for folder in element:
            clone += folder
            try:
                for filename in os.listdir(clone):






                    text = filename.lower()

                    for sign in sonderzeichen:
                        text = text.replace(sign, " ")

                    liste = text.split()

                    for word in liste:

                        if not (word in vokabelbuch.keys()):

                            vokabelbuch[word] = 1

                        else:

                            vokabelbuch[word] += 1





            except UnicodeDecodeError:
                # to do: find different encoding way
                pass
            clone = path

    return vokabelbuch
