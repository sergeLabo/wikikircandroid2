#!/usr/bin/python3
# -*- coding: UTF-8 -*-


note_dict = {   '0':0,  '1':35,  '2':2,  '3':34,  '4':4,  '5':33,
                'a':6,  'b':7,  'c':8,  'd':9,  'e':10, 'f':11,
                'g':12, 'h':13, 'i':14, 'j':15, 'k':16, 'l':17,
                'm':18, 'n':19, 'o':20, 'p':21, 'q':22, 'r':23,
                's':24, 't':25, 'u':26, 'v':27, 'w':28, 'x':29,
                'y':30, 'z':31, '6':32, '7':1, '8':3, '9':5
            }

# modifie le rythm des notes
correction = 1.4

class Note:
    """
    Un objet par ligne:
    
    """
    
    def __init__(self, line):
        self.line = line
        self.length = len(line)
        self.get_every()
        self.progress = 0
        self.note = None
        self.volume = 0
        
    def get_every(self):
        """Une note est jouee tous les every update_clock=0.03s
        Plus la ligne est longue, plus je joue vite
        TODO calcul fonction de update_clock ?
        """
        
        global correction
        
        self.every = 6
        
        if self.length < 30:
            self.every = 9
        if 31 < self.length < 100:
            self.every = 8
        if 101 < self.length < 200:
            self.every = 7
        if 201 < self.length < 300:
            self.every = 6
        if 301 < self.length < 400:
            self.every = 5
        if 400 < self.length:
            self.every = 4
            
        # TODO correction fonction de update_clock
        self.every = int(self.every*correction)
        
    def get_note(self):
        # A chaque tour de boucle
        self.progress += 1
        
        # je joue tous les every
        if self.progress % self.every == 1:
            # Je joue la note de la lettre en position self.progress
            if self.progress < self.length - 1:
                if self.line[self.progress] in list(note_dict.keys()):
                    self.note = note_dict[self.line[self.progress]]
        
        # self.note mis a jour une seule fois
        else:
            self.note = None
            
        return self.note
        
    def get_volume(self):
        # set du volume pour la ligne
        n = min(self.length, 500)
        self.vol = 0.1 + 0.9 * n/500
        
        return self.vol

    
    
if __name__ == "__main__":
    
    from time import sleep
    
    str1 = """La commissaire europeenne chargee des Relations exterieures, 
    l'Autrichienne  Benita Ferrero-Waldner  annonce qu'elle espere un 
    acheminement rapide de l'aide humanitaire mais avertit qu'il n'y aura 
    aucun effort de reconstruction a Gaza tant que le Hamas sera au pouvoir 
    ref  lien web url http: www.lefigaro.fr international 2009 01 19 
    01003-20090119ARTFIG00444-retour-au-calme-a-gaza-.php titre Gaza : 
    Abbas propose un gouvernement avec le Hamas editeur Le Figaro date 
    19 janvier 2009 consulte le 19 janvier 2009  ref ."""
    
    j = 0
    phrase_note = Note(str1)
    
    while j < len(str1):
        j += 1
        sleep(0.03)
        
        note = phrase_note.get_note()
        volume = phrase_note.get_volume()
        if note:
            print(j, note, volume)
