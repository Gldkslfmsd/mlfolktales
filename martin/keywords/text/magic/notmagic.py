import os


def notanimal():
    vokabelbuch = {}


    path = "../../../../Fairytale Corpus/English/"

    sonderzeichen = ['.', ',', '"', '?', '-', '!', "'", ':', ';', '—', '[', ']']

    clone = path

    Animal = ["Animal Tales/Domestic Animals",
              "Animal Tales/Other Animals and Objects",
              "Animal Tales/Wild Animals",
              "Animal Tales/Wild Animals and Domestic Animals",
              "Animal Tales/Wild Animals and Humans"]
    Anecdotes = ["Anecdotes and Jokes/Jokes about Clergymen and Religious Figures",
              "Anecdotes and Jokes/Stories about a Fool",
              "Anecdotes and Jokes/Stories about a Man",
              "Anecdotes and Jokes/Stories about a Woman",
              "Anecdotes and Jokes/Stories about Married Couples",
              "Anecdotes and Jokes/Tall Tales"]
    Formula = ["Formula Tales/Catch Tales",
              "Formula Tales/Cumulative Tales"
              ]
    Realistic = ["Realistic Tales/Clever Acts and Words",
              "Realistic Tales/Proofs of Fidelity and Innocence",
              "Realistic Tales/Robbers and Murderers",
              "Realistic Tales/Tales of Fate",
              "Realistic Tales/The Man Marries the Princess",
              "Realistic Tales/The Obstinate Wife Learns to Obey",
              "Realistic Tales/The Woman Marries the Prince",
              ]
    Religious = ["Religious Tales/God Rewards and Punishes", "Religious Tales/Heaven",
              "Religious Tales/Other Religious Tales", "Religious Tales/The Devil",
              "Religious Tales/The Truth Comes to Light"]
    Ogre = ["Tales of the Stupid Ogre/Labor Contract", "Tales of the Stupid Ogre/Man Kills (Injures) Ogre",
            "Tales of the Stupid Ogre/Man Outwits the Devil",
            "Tales of the Stupid Ogre/Partnership between Man and Ogre",
            "Tales of the Stupid Ogre/Souls Saved from the Devil"]
    Unknown = ["UNKNOWN"]

    pathlist = [Animal, Anecdotes, Formula, Realistic, Religious, Ogre, Unknown]

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

#





