from __future__ import unicode_literals
from kivymd.app import MDApp
from kivy.lang.builder import Builder as New
from kivy.uix.screenmanager import Screen
#from kivymd.uix.dialog import MDDialog
#import auto_py_to_exe



from kivymd.uix.button import MDFlatButton,MDRectangleFlatIconButton,MDIconButton,MDRaisedButton,MDFloatingActionButton,MDFillRoundFlatIconButton
#from kivymd.uix.button import MDRectangleFlatButton,MDCustomRoundIconButton,MDRoundFlatIconButton,MDFlatButton
from kivymd.uix.textfield import MDTextField,MDTextFieldRound
from kivymd.uix.label import MDLabel,MDIcon
#from kivymd.uix.progressbar import MDProgressBar
from kivymd.uix.dialog import MDDialog
from kivymd.toast import toast
from helpers import KV
from tkinter.filedialog import askdirectory
import requests
import json

from fpdf import FPDF

from tkinter import Tk
import youtube_dl
import os



class Myscreen(Screen):
    pass


class Builder(MDApp):
    def build(self, *args):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_hue='A400'
        self.theme_cls.primary_palette='Green'
        self.screen=New.load_string(KV)
        return  self.screen

    def back_screen(self):
        MDApp.get_running_app().root.transition.direction = 'right'
        MDApp.get_running_app().root.current = 'menu'


    def lyrics_to_pdf(self):

        self.lyric_downloaded=False
        self.song = self.screen.ids.songname.text
        self.artist = self.screen.ids.artistname.text


        if(self.song=='' or self.artist==''):
            close_btn = MDRaisedButton(text='Close', on_release=self.check_for_blank_close)
            self.blank_check_dialogue = MDDialog(title='Please enter values', buttons=[close_btn])
            self.blank_check_dialogue.open()




        else:


            artist_name = self.screen.ids.artistname.text
            song_name = self.screen.ids.songname.text

            url = 'https://api.lyrics.ovh/v1/' + artist_name + '/' + song_name

            # fetch lyrics
            try:
                responce = requests.get(url)
                json_data = json.loads(responce.content)
                lyrics = json_data.get('lyrics', None)




                if lyrics==None:

                    close_btn = MDRaisedButton(text='Close', on_release=self.check_for_blank_close)
                    self.blank_check_dialogue = MDDialog(title='Song not found',text='Try checking  the spelling of entered quantinties ', buttons=[close_btn])
                    self.blank_check_dialogue.open()
                else:
                    files = [('text file', '*.txt')]
                    root = Tk()
                    root.withdraw()
                    file = askdirectory()
                    print(file)

                    # text_file_location= f'E:\lyrics\{song_name}.txt'
                    text_file_location = f'{file}/{song_name}.txt'
                    file1 = open(text_file_location, 'w+')
                    file1.write(lyrics)
                    file1.close()

                    os.chdir(file)

                    # text_file_location=f'E:\lyrics/{song_name}.txt'

                    # save FPDF() class into
                    # a variable pdf
                    pdf = FPDF()

                    # Add a page
                    pdf.add_page()

                    # set style and size of font
                    # that you want in the pdf
                    pdf.set_font("Arial", size=12)

                    # open the text file in read mode
                    f = open(text_file_location, "r")

                    # insert the texts in pdf
                    for x in f:
                        pdf.cell(200, 10, txt=x, ln=1, align='C')

                    # save the pdf with name .pdf
                    pdf.output(f'{song_name}.pdf')

                    self.lyric_downloaded=True

                    if(self.lyric_downloaded==True):
                        self.lyric_downloaded_popup()


            except :
                close_btn = MDRaisedButton(text='Close', on_release=self.check_for_blank_close)
                self.blank_check_dialogue = MDDialog(title='Error',text='Please check your internet connection', buttons=[close_btn])
                self.blank_check_dialogue.open()


    def mp3_download(self):
        self.mp3_downloaded=False

        #download_postion = 'E:/things'



        link = self.screen.ids.youtubelink.text

        if (link == '' ):
            close_btn = MDRaisedButton(text='Close', on_release=self.check_for_blank_close)
            self.blank_check_dialogue = MDDialog(title='Copy the Youtube link', buttons=[close_btn])
            self.blank_check_dialogue.open()

        elif self.check_internet_connection():

            files = [('text file', '*.txt')]
            root = Tk()
            root.withdraw()
            download_postion = askdirectory()


            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }

            os.chdir(download_postion)
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:

                    try:
                        ydl.download([link])
                        self.mp3_downloaded=True

                    except:

                        self.mp3_downloaded_popup()





        else:
            close_btn = MDRaisedButton(text='Close', on_release=self.check_for_blank_close)
            self.blank_check_dialogue = MDDialog(title='Song not found',
                                                 text='Try checking your network connection',
                                                 buttons=[close_btn])
            self.blank_check_dialogue.open()

    def mp4_download(self):

        mp4_downloaded=False

        link = self.screen.ids.youtubelink.text

        if (link == ''):
            close_btn = MDRaisedButton(text='Close', on_release=self.check_for_blank_close)
            self.blank_check_dialogue = MDDialog(title='Copy the Youtube link', buttons=[close_btn])
            self.blank_check_dialogue.open()

        elif self.check_internet_connection():

            files = [('text file', '*.txt')]
            root = Tk()
            root.withdraw()
            download_postion = askdirectory()

            ydl_opts = {}

            #download_postion = 'E:/things'
            os.chdir(download_postion)


            try:

                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([link])
                    mp4_downloaded=True
                    self.mp4_downloaded_popup()

            except:
                close_btn = MDRaisedButton(text='Close', on_release=self.check_for_blank_close)
                self.blank_check_dialogue = MDDialog(title='Song not found',
                                                     text='Try checking the link given',
                                                     buttons=[close_btn])
                self.blank_check_dialogue.open()




        else:
            close_btn = MDRaisedButton(text='Close', on_release=self.check_for_blank_close)
            self.blank_check_dialogue = MDDialog(title='Song not found',
                                                 text='Try checking your network connection',
                                                 buttons=[close_btn])
            self.blank_check_dialogue.open()




    def check_for_blank_close(self,obj):
        self.blank_check_dialogue.dismiss()

    def lyric_downloaded_popup(self):
        toast('Lyrics succesfully downloaded')

    def mp3_downloaded_popup(self):
        toast('Mp3 succesfully downloaded')

    def mp4_downloaded_popup(self):
        toast('Mp4 succesfully downloaded')

    def check_internet_connection(self):
        try:
            requests.get('https://google.com')
            return True
        except:
            return  False

    def downloading_popup(self):
        toast('Downloading')





Builder().run()


