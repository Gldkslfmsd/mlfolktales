import os
import fnmatch



def animal():

    vokabelbuch = {}

    path = "../../../Fairytale Corpus/English/"

    sonderzeichen = ['.', ',', '"', '?', '-', '!', "'", ':', ';', '—', '[', ']']

    clone = path

    Animal = [ "Animal Tales/Domestic Animals",
	"Animal Tales/Other Animals and Objects",
	"Animal Tales/Wild Animals",
	"Animal Tales/Wild Animals and Domestic Animals",
	"Animal Tales/Wild Animals and Humans"]



    pathlist = [Animal]

    for element in pathlist:

        for folder in element:
            i=0
            clone += folder
            try:
                for filename in os.listdir(clone):
                    
                        lines = open(clone + "/" + filename, "r").readlines()

                        del lines [0]
                        del lines [0]
                        del lines [0]
                        del lines [0]

                        #lines enthält jetzt nur noch ein element, welches den text einer geschichte enthält


            

                        text = lines[0].lower()
                
                        for sign in sonderzeichen:

                            text = text.replace(sign," ")

                        liste = text.split()

            

                        for word in liste:

                            if not (word in vokabelbuch.keys()):

                                vokabelbuch[word] = 1

                            else:

                                vokabelbuch[word] += 1
                    
         
            
           
            
            except UnicodeDecodeError:
                #to do: find different encoding way
                pass
            clone = path
    
            
    return vokabelbuch
