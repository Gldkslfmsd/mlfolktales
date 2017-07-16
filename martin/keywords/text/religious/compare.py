import religious
import notreligious

keyworddict = {}

#tiere ist dict
tiere = religious.animal()

#anderes ist dict
anderes = notreligious.notanimal()



#schreibt alles aus den animal-keywords in keywords.txt,
#das 0-mal in notanimal.txt vorkommt, oder öfter in animal
#vorkommt als in notanimal


for element in tiere:

    if not(element in anderes.keys()):

        keyworddict[element] = tiere[element]

    else:

        if (tiere[element] > anderes[element]):

            keyworddict[element] = tiere[element]

file = open("religiouskeywordstext.txt", "w")

for a in keyworddict:

    if keyworddict[a] >= 10:

        file.write(a + "  -  " + str(keyworddict[a]) + "\n")

file.close()
