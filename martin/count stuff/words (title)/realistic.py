import os


#gibt durchschnittliche wörtliche reden pro text zurück
def word():

    ratio = 0

    count = 0

    vokabelbuch = {}

    path = "C:\\Users\\Martin\\Desktop\\git python\\mlfolktales-master\\Fairytale Corpus\\English\\"

    sonderzeichen = ['.', ',', '"', '?', '-', '!', "'", ':', ';', '—', '[', ']']

    clone = path

    Realistic = ["Realistic Tales\\Clever Acts and Words","Realistic Tales\\Proofs of Fidelity and Innocence","Realistic Tales\\Robbers and Murderers","Realistic Tales\\Tales of Fate","Realistic Tales\\The Man Marries the Princess","Realistic Tales\\The Obstinate Wife Learns to Obey","Realistic Tales\\The Woman Marries the Prince"]
    
    pathlist = [Realistic]

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



    

