import os


#gibt durchschnittliche wörtliche reden pro text zurück
def word():

    ratio = 0

    count = 0

    vokabelbuch = {}

    path = "C:\\Users\\Martin\\Desktop\\git python\\mlfolktales-master\\Fairytale Corpus\\English\\"

    sonderzeichen = ['.', ',', '"', '?', '-', '!', "'", ':', ';', '—', '[', ']']

    clone = path

    Unknown = ["UNKNOWN"]

    pathlist = [Unknown]

    for element in pathlist:

        for folder in element:
    
            clone += folder
            try:
                for filename in os.listdir(clone):

                    lines = open(clone + "\\" + filename, "r").readlines()

                    del lines [0]
                    del lines [0]
                    del lines [0]
                    del lines [0]

                    #lines enthält jetzt nur noch ein element, welches den text einer geschichte enthält


            

                    text = lines[0].lower()
                
                    for sign in sonderzeichen:

                        text = text.replace(sign," ")

                    liste = text.split()

            

                    count += len(liste)
                    
                    ratio += 1
    
         
            except UnicodeDecodeError:
                #to do: find different encoding way
                pass
            clone = path
        
    return count/ratio



    


