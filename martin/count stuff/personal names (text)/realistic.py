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

    Realistic = ["Realistic Tales\\Clever Acts and Words", "Realistic Tales\\Proofs of Fidelity and Innocence",
                 "Realistic Tales\\Robbers and Murderers", "Realistic Tales\\Tales of Fate",
                 "Realistic Tales\\The Man Marries the Princess", "Realistic Tales\\The Obstinate Wife Learns to Obey",
                 "Realistic Tales\\The Woman Marries the Prince"]

    pathlist = [Realistic]

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






