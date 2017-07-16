import os
import fnmatch


def animal():
    vokabelbuch = {}

    path = "../../../../Fairytale Corpus/English/"

    sonderzeichen = ['.', ',', '"', '?', '-', '!', "'", ':', ';', '—', '[', ']']

    clone = path
    Animal = ["Tales of the Stupid Ogre/Labor Contract", "Tales of the Stupid Ogre/Man Kills (Injures) Ogre",
            "Tales of the Stupid Ogre/Man Outwits the Devil",
            "Tales of the Stupid Ogre/Partnership between Man and Ogre",
            "Tales of the Stupid Ogre/Souls Saved from the Devil"]



    pathlist = [Animal]

    for element in pathlist:

        for folder in element:
            i = 0
            clone += folder
            try:
                for filename in os.listdir(clone):

                    lines = open(clone + "/" + filename, "r").readlines()

                    del lines[0]
                    del lines[0]
                    del lines[0]
                    del lines[0]

                    # lines enthält jetzt nur noch ein element, welches den text einer geschichte enthält




                    text = lines[0].lower()

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
