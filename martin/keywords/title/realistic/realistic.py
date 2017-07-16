import os
import fnmatch


def animal():
    vokabelbuch = {}

    path = "../../../../Fairytale Corpus/English/"

    sonderzeichen = ['.', ',', '"', '?', '-', '!', "'", ':', ';', '—', '[', ']']

    clone = path

    Animal = ["Realistic Tales/Clever Acts and Words",
              "Realistic Tales/Proofs of Fidelity and Innocence",
              "Realistic Tales/Robbers and Murderers",
              "Realistic Tales/Tales of Fate",
              "Realistic Tales/The Man Marries the Princess",
              "Realistic Tales/The Obstinate Wife Learns to Obey",
              "Realistic Tales/The Woman Marries the Prince",
             ]

    pathlist = [Animal]

    for element in pathlist:

        for folder in element:
            i = 0
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
