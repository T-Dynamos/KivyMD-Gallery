from kivy.lang import Builder 
from kivy.core.window import Window
from kivymd.tools.hotreload.app import MDApp
from kivy.metrics import dp
from kivymd.uix.behaviors import *
from kivymd.uix.card import MDCard
from kivy.animation import Animation
from kivymd.uix.templates import RotateWidget
from kivymd.uix.button import *
from kivy.clock import Clock 
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.label import MDLabel
from kivymd.toast import toast as Toast

Window.size = [dp(400),dp(600)]

class Card(MDCard,FakeRectangularElevationBehavior):
    pass

class CardCircular(MDCard,FakeCircularElevationBehavior):
    pass

class IconButton(MDIconButton,RotateWidget):
    pass

class Image2(Image,RotateWidget):
    pass


class LoginScreen(MDApp):

    x = Window.size[0]
    y = Window.size[1]

    manager = ScreenManager()

    file_read = open("main.kv","r").read()
    hotreload = True
    label =  None

    def build(self):
        self.manager.add_widget(Builder.load_string(self.file_read))
        return self.manager

    def change_type(self,instance):
        anim = Animation(
            opacity=0,
            d=0.3
            )
        anim2 = Animation(
            size=(self.x-dp(40),dp(200)),
            d=0.3
            )
        anim3 = Animation(
            size=(self.x-dp(40),dp(150)),
            d=0.3
            )
        def run(*largs):
            instance.opacity = 1
            instance.pos_hint = {"center_x":0.99,"center_y":0.7}
            self.manager.get_screen("main").ids.test2.text = "Register"
            self.manager.get_screen("main").ids.test_box.pos_hint = {"center_x":0.46,"center_y":0.56}
            self.manager.get_screen("main").ids.test_box.opacity = 1
            self.manager.get_screen("main").ids.text_label.opacity = 0        
        def run2(*largs):
            instance.opacity = 1
            instance.pos_hint = {"center_x":-0.005,"center_y":0.25}
            self.manager.get_screen("main").ids.test_box.pos_hint = {"center_x":0.0,"center_y":0.55}
            self.manager.get_screen("main").ids.test_box.opacity = 0
            self.manager.get_screen("main").ids.test2.text = "Login"
            self.manager.get_screen("main").ids.text_label.opacity = 1

        if self.manager.get_screen("main").ids.test2.text == "Login":
            anim2.start(self.manager.get_screen("main").ids.my_card)
            anim.start(instance)
            anim.bind(on_complete=run)
        else:
            anim3.start(self.manager.get_screen("main").ids.my_card)
            anim.start(instance)
            anim.bind(on_complete=run2)


    def call_animation(self,instance,*largs):
        anim = Animation(
            rotate_value_angle=-360, 
            d=0.3
                )
        anim2 = Animation(
            opacity=0,
            d=0.3
                )
        anim.start(instance)
        def change_icon(*largs):
            instance.icon = "check" if instance.icon == "arrow-right" else "arrow-right"
            instance.opacity = 1
            instance.rotate_value_angle = 1
            #Toast(self.manager.get_screen("main").ids.username+" "+self.manager.get_screen("main").ids.email+" "+self.manager.get_screen("main").ids.password)
        anim2.start(instance)
        anim2.bind(on_complete=change_icon)

        def on_start(self):
            self.label = Builder.load_string(
"""
MDBoxLayout:
    size_hint:None,None
    size:(app.x-dp(40))-dp(50),dp(80)
    md_bg_color:0,0,0,0
    MDIconButton:
        icon:"email"
    MDTextField:
        hint_text: "mail"
"""

                )

LoginScreen().run()

