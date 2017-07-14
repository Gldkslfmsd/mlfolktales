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

    Magic = ["Tales of Magic\\Magic Objects", "Tales of Magic\\Other Tales of the Supernatural",
             "Tales of Magic\\Supernatural Adversaries", "Tales of Magic\\Supernatural Helpers",
             "Tales of Magic\\Supernatural or Enchanted Wife (Husband) or Other Relative",
             "Tales of Magic\\Supernatural Power or Knowledge", "Tales of Magic\\Supernatural Tasks"]

    pathlist = [Magic]

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






