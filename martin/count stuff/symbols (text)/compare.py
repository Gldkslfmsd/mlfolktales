import animal
import notanimal
import anecdotes
import formula
import magic
import ogre
import realistic
import religious
import unknown

file = open("sonderzeichen pro text.txt", "w")

file.write("other stories: " + str(notanimal.countnotanimalsymbol())+"\n\n")

file.write("animal stories: " + str(animal.countanimalsymbol())+"\n")
file.write("anecdote stories: " + str(anecdotes.countanecdotesymbol())+"\n")
file.write("formula stories: " + str(formula.countformulasymbol())+"\n")
file.write("magic stories: " + str(magic.countmagicsymbol())+"\n")
file.write("ogre stories: " + str(ogre.countogresymbol())+"\n")
file.write("realistic stories: " + str(realistic.countrealisticsymbol())+"\n")
file.write("religious stories: " + str(religious.countreligioussymbol())+"\n")
file.write("unknown stories: " + str(unknown.countunknownsymbol()))


file.close()
