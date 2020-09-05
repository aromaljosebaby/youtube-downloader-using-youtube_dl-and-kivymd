KV = """
#:import MDFillRoundFlatButton kivymd.uix.button.MDFillRoundFlatButton
#:import MDProgressBar kivymd.uix.progressbar.MDProgressBar



ScreenManager:
    Screen:
        name: "menu"


        MDLabel:
            text:'Music Bae'
            halign:'center'
            pos_hint:{'center_x':0.5,'center_y':0.9} 
            theme_text_color:'Custom'
            text_color: 1,1,1,0.9
            font_style: 'H4'







        MDTextField:
            id:songname
            hint_text:'Enter song name'  
            pos_hint:{'center_x':0.6,'center_y':0.65} 
            size_hint_x:None 
            width:300
            icon_right:'lock'
            icon_right_color:app.theme_cls.primary_color

        MDTextField:
            id:artistname
            hint_text:'Enter Artist name'  
            pos_hint:{'center_x':0.6,'center_y':0.5} 
            size_hint_x:None 
            width:300
            icon_right:'music-note'
            icon_right_color:app.theme_cls.primary_color

        MDRaisedButton:
            text:  "Lyrics"
            pos_hint:{'center_x':0.2,'center_y':0.3}
            on_release: app.root.current = "menu"
            on_release: app.lyrics_to_pdf()




        MDRaisedButton:
            text: " Song"
            pos_hint:{'center_x':0.8,'center_y':0.3}
            on_release: app.root.current = "myscreen"



        MDIconButton:

            pos_hint:{'center_x':0.2,'center_y':0.575}
            icon:'images/leopard.png'
            md_bg_color:1,1,1,0.9 
            user_font_size:'100sp'
            
        MDIconButton:

            pos_hint:{'center_x':0.37,'center_y':0.905}
            icon:'images/leaf (1).png'
            md_bg_color:1,1,1,0.9 
            user_font_size:'21sp'    
















    Myscreen
        name: "myscreen"


        MDTextField:
            id:youtubelink
            hint_text:'Paste the Youtube link here'
            mode:'fill'
            fill_color:0,0,0,0.5
            pos_hint:{'center_x':0.5,'center_y':0.6} 
            size_hint_x:None 
            width:600
            normal_color:app.theme_cls.primary_color
            icon_right:'lock'
            icon_right_color:app.theme_cls.primary_color    

        MDRaisedButton:
            text: " Go back"
            pos_hint:{'center_x':0.5,'center_y':0.2}
            on_release: app.root.current = "menu"   




        MDRaisedButton:
            text: " MP4"
            pos_hint:{'center_x':0.8,'center_y':0.45}
            icon:'reply'
            on_release: app.mp4_download()    

        MDRaisedButton:
            text: " MP3"
            pos_hint:{'center_x':0.2,'center_y':0.45}
            icon:'reply'
            on_release: app.mp3_download()  
            
        MDIconButton:

            pos_hint:{'center_x':0.5,'center_y':0.8}
            icon:'images/panda.png'
            md_bg_color:1,1,1,0.9 
            user_font_size:'90sp'    





"""
