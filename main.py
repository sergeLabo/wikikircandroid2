#! /usr/bin/env python2
# -*- coding: utf-8 -*-

# Pas d'accent pour mettre toute les chances de mon cote à la compil

########################################################################
# This file is part of wikikircandroid2.
#
# wikikircandroid2 is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# wikikircandroid2 is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
########################################################################


from os import _exit
from threading import Thread
import textwrap

import kivy
kivy.require('1.10.0')

from kivy.core.window import Window

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ListProperty
from kivy.properties import StringProperty
from kivy.clock import Clock
from kivy.core.audio import SoundLoader

from wikikIRC2 import MyIRCBot
from note import Note


from sys import platform

# non inclus dans apk version 0.5
print("Platform = {}".format(platform))

# Window size sur PC
if platform == 'linux2':
    k = 0.6
    WS = (int(720*k), int(1280*k))
    Window.size = WS

    
class WikikIRC:

    def __init__(self):

        print("Initialisation de WikikIRC ok")

        server_list = [("irc.wikimedia.org",  6667)]
        channel = "#fr.wikipedia"
        nickname = "La Labomedia"
        realname = "Syntaxis analysis with Python bot"
    
        # Tourne tout le temps
        self.bot = MyIRCBot(server_list, 
                            channel, 
                            nickname, 
                            realname, 
                            bavard=False)
                            
        # Boucle infinie pour envoi continu a tous les joueurs
        self.get_modif_thread()

    def get_modif(self):
        self.bot.start()
        
    def get_modif_thread(self):
        thread_s = Thread(target=self.get_modif)
        thread_s.start()


class MainScreen(Screen, WikikIRC):
    """Ecran principal"""
    
    info = StringProperty()
    volume = NumericProperty(1.0)
    f_size = NumericProperty(18) #36)
    
    def __init__(self, **kwargs):
        Screen.__init__(self, **kwargs)
        WikikIRC.__init__(self)
        
        self.info = "Patience et longueur de temps font plus que force ni que rage !"
        self.f_size = 18 #36
        
        # Chargement des sons
        self.notes = {}
        for i in range(36):
            self.notes[i] = SoundLoader.load(   './samples/' + 
                                                str(i) + 
                                                '.ogg')
        
        # Rafraichissement du jeu
        tempo = 0.03
        
        self.event = Clock.schedule_interval(self.wikirc_update, tempo)   
                  
        print("Initialisation de MainScreen ok")
        
    def wikirc_update(self, dt):

        # Pour nouvel info
        info_old = self.info
        
        # Sortie IRC
        try:
            wo = self.bot.wiki_out
            
            if 600 < len(wo) <= 1000:
                self.f_size = 14 #28
                ln = 50
            elif 1000 < len(wo) <= 1400:
                self.f_size = 12 #24
                ln = 60
            elif 1400 < len(wo) <= 1800:
                self.f_size = 10 #20
                ln = 70
            elif 1800 < len(wo):
                self.f_size = 9 #18
                ln = 80
            else:
                self.f_size = 18 #36
                ln = 40
        except:
            self.info = "Patience et longueur de temps font plus que force ni que rage !"
        
        self.info = textwrap.fill(wo, ln)
        
        # Si un nouvel info, donc une seule fois par info
        if self.info != info_old:
            self.phrase_note = Note(self.info)
            
        n = self.phrase_note.get_note()
        self.volume = self.phrase_note.get_volume()
        
        if n:
            self.sound(n)
        
    def sound(self, n):
        """Joue la note n"""
        
        self.notes[n].volume = self.volume
        self.notes[n].play()
            
    def get_sm(self):
        return WikikircAndroidApp.get_running_app().sm


class WikikircAndroidApp(App):
    """Construction de l'application. Execute par __main__"""

    def build(self):
        """Execute en premier apres run()"""

        # Creation des ecrans
        self.sm = ScreenManager()
        self.sm.add_widget(MainScreen(name="Main"))

        return self.sm

    def build_config(self, config):
        """Si le fichier *.ini n'existe pas,
        il est cree avec ces valeurs par defaut.
        Si il manque seulement des lignes, il ne fait rien !
        """

        config.setdefaults('kivy',
                            { 'log_level': 'debug',
                              'log_name': 'multipong_%y-%m-%d_%_.txt',
                              'log_dir': '/sdcard',
                              'log_enable': '1'})

        config.setdefaults('postproc',
                            { 'double_tap_time': 250,
                              'double_tap_distance': 20})

    def go_mainscreen(self):
        """Retour au menu principal depuis les autres ecrans."""

        #if touch.is_double_tap:
        self.sm.current = ("Main")

    def do_quit(self):

        print("Je quitte proprement")

        # Stop propre de Clock
        menu = self.sm.get_screen("Main")
        menu.event.cancel()

        # Kivy
        WikikircAndroidApp.get_running_app().stop()

        # Extinction de tout
        _exit(0)


if __name__ == '__main__':
    WikikircAndroidApp().run()
