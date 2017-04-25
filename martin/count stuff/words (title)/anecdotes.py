import os


#gibt durchschnittliche wörtliche reden pro text zurück
def word():

    ratio = 0

    count = 0
    
    vokabelbuch = {}

    path = "C:\\Users\\Martin\\Desktop\\git python\\mlfolktales-master\\Fairytale Corpus\\English\\"

    sonderzeichen = ['.', ',', '"', '?', '-', '!', "'", ':', ';', '—', '[', ']']

    clone = path

    Anecdotes = ["Anecdotes and Jokes\\Jokes about Clergymen and Religious Figures","Anecdotes and Jokes\\Stories about a Fool","Anecdotes and Jokes\\Stories about a Man","Anecdotes and Jokes\\Stories about a Woman","Anecdotes and Jokes\\Stories about Married Couples","Anecdotes and Jokes\\Tall Tales"]
    


    pathlist = [Anecdotes]

    for element in pathlist:

        for folder in element:
    
            clone += folder
            try:
                for filename in os.listdir(clone):

                    for sign in sonderzeichen:

                        text = filename.replace(sign," ")

                    liste = text.split()

            

                    count += len(liste)
                    
                    ratio += 1
            
            except UnicodeDecodeError:
                #to do: find different encoding way
                pass
            clone = path
    
            
    return count/ratio


