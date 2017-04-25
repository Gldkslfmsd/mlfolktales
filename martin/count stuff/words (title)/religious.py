import os


#gibt durchschnittliche wörtliche reden pro text zurück
def word():

    ratio = 0

    count = 0

    vokabelbuch = {}

    path = "C:\\Users\\Martin\\Desktop\\git python\\mlfolktales-master\\Fairytale Corpus\\English\\"

    sonderzeichen = ['.', ',', '"', '?', '-', '!', "'", ':', ';', '—', '[', ']']

    clone = path

    Religious = ["Religious Tales\\God Rewards and Punishes","Religious Tales\\Heaven","Religious Tales\\Other Religious Tales","Religious Tales\\The Devil","Religious Tales\\The Truth Comes to Light"]
    
    pathlist = [Religious]

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



    


