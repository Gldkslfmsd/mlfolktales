import os
import fnmatch


def animal():
    vokabelbuch = {}

    path = "../../../../Fairytale Corpus/English/"

    sonderzeichen = ['.', ',', '"', '?', '-', '!', "'", ':', ';', '—', '[', ']']

    clone = path
    Animal = ["Tales of Magic/Magic Objects", "Tales of Magic/Other Tales of the Supernatural",
             "Tales of Magic/Supernatural Adversaries", "Tales of Magic/Supernatural Helpers",
             "Tales of Magic/Supernatural or Enchanted Wife (Husband) or Other Relative",
             "Tales of Magic/Supernatural Power or Knowledge", "Tales of Magic/Supernatural Tasks"]


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
