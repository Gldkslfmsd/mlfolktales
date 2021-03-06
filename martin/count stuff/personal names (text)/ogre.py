import os
from nltk.tag import pos_tag


# gibt durchschnittliche wörtliche reden pro text zurück
def word():
    ratio = 0

    count = 0

    vokabelbuch = {}

    path = "../../../Fairytale Corpus/English/"
    sonderzeichen = ['.', ',', '"', '?', '-', '!', "'", ':', ';', '—', '[', ']']

    clone = path

    Ogre = ["Tales of the Stupid Ogre\\Labor Contract", "Tales of the Stupid Ogre\\Man Kills (Injures) Ogre",
            "Tales of the Stupid Ogre\\Man Outwits the Devil",
            "Tales of the Stupid Ogre\\Partnership between Man and Ogre",
            "Tales of the Stupid Ogre\\Souls Saved from the Devil"]

    pathlist = [Ogre]

    for element in pathlist:

        for folder in element:

            clone += folder
            try:
                for filename in os.listdir(clone):

                    lines = open(clone + "\\" + filename, "r").readlines()

                    del lines[0]
                    del lines[0]
                    del lines[0]
                    del lines[0]

                    # lines enthält jetzt nur noch ein element, welches den text einer geschichte enthält




                    text = lines[0]

                    tagged_sent = pos_tag(text.split())

                    propernouns = [word for word, pos in tagged_sent if pos == 'NNP']

                    count += len(propernouns)

                    ratio += 1


            except UnicodeDecodeError:
                # to do: find different encoding way
                pass
            clone = path

    return count / ratio






