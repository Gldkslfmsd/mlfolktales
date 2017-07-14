import animal
import notanimal
import anecdotes
import formula
import magic
import ogre
import realistic
import religious
import unknown

file = open("eigennamen pro text.txt", "w")

file.write("other stories: " + str(notanimal.word())+"\n\n")

file.write("animal stories: " + str(animal.word())+"\n")
file.write("anecdote stories: " + str(anecdotes.word())+"\n")
file.write("formula stories: " + str(formula.word())+"\n")
file.write("magic stories: " + str(magic.word())+"\n")
file.write("ogre stories: " + str(ogre.word())+"\n")
file.write("realistic stories: " + str(realistic.word())+"\n")
file.write("religious stories: " + str(religious.word())+"\n")
file.write("unknown stories: " + str(unknown.word()))


file.close()
