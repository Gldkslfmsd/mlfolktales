from nltk.tag import pos_tag
import os


# gibt durchschnittliche eigennamen pro text zurück

def word():

    ratio = 0

    count = 0

    vokabelbuch = {}

    path = "../../../Fairytale Corpus/English/"
    sonderzeichen = ['.', ',', '"', '?', '-', '!', "'", ':', ';', '—', '[', ']']

    clone = path

    Anecdotes = ["Anecdotes and Jokes\\Jokes about Clergymen and Religious Figures",
                 "Anecdotes and Jokes\\Stories about a Fool", "Anecdotes and Jokes\\Stories about a Man",
                 "Anecdotes and Jokes\\Stories about a Woman", "Anecdotes and Jokes\\Stories about Married Couples",
                 "Anecdotes and Jokes\\Tall Tales"]

    pathlist = [Anecdotes]

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