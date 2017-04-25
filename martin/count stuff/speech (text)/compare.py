import animal
import notanimal
import anecdotes
import formula
import magic
import ogre
import realistic
import religious
import unknown

file = open("wörtliche rede pro text.txt", "w")

file.write("other stories: " + str(notanimal.countnotanimalspeech())+"\n\n")

file.write("animal stories: " + str(animal.countanimalspeech())+"\n")
file.write("anecdote stories: " + str(anecdotes.countanecdotespeech())+"\n")
file.write("formula stories: " + str(formula.countformulaspeech())+"\n")
file.write("magic stories: " + str(magic.countmagicspeech())+"\n")
file.write("ogre stories: " + str(ogre.countogrespeech())+"\n")
file.write("realistic stories: " + str(realistic.countrealisticspeech())+"\n")
file.write("religious stories: " + str(religious.countreligiousspeech())+"\n")
file.write("unknown stories: " + str(unknown.countunknownspeech()))


file.close()
