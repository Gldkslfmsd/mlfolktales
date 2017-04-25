import animal
import notanimal
import anecdotes
import formula
import magic
import ogre
import realistic
import religious
import unknown

file = open("satzzahl pro text.txt", "w")

file.write("other stories: " + str(notanimal.sentences())+"\n\n")

file.write("animal stories: " + str(animal.sentences())+"\n")
file.write("anecdote stories: " + str(anecdotes.sentences())+"\n")
file.write("formula stories: " + str(formula.sentences())+"\n")
file.write("magic stories: " + str(magic.sentences())+"\n")
file.write("ogre stories: " + str(ogre.sentences())+"\n")
file.write("realistic stories: " + str(realistic.sentences())+"\n")
file.write("religious stories: " + str(religious.sentences())+"\n")
file.write("unknown stories: " + str(unknown.sentences()))


file.close()
