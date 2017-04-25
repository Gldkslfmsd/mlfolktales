import animal
import notanimal

keyworddict = {}

#tiere ist dict
tiere = animal.animal()

#anderes ist dict
anderes = notanimal.notanimal()



#schreibt alles aus den animal-keywords in keywords.txt,
#das 0-mal in notanimal.txt vorkommt, oder öfter in animal
#vorkommt als in notanimal


for element in tiere:

    if not(element in anderes.keys()):

        keyworddict[element] = tiere[element]

    else:

        if (tiere[element] > anderes[element]):

            keyworddict[element] = tiere[element]

print(keyworddict)

file = open("keywordstext.txt", "w")

for a in keyworddict:

    file.write(a + "  -  " + str(keyworddict[a]) + "\n")

file.close()
