from kivy.config import Config
Config.set('graphics', 'resizable', 1)
Config.set('graphics', 'width', 320)
Config.set('graphics', 'heigth', 1000)
from kivymd.app import MDApp 
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFloatingActionButton, MDFloatingActionButtonSpeedDial, MDRoundFlatIconButton, MDIconButton
from kivy.lang import Builder
from kivy.uix.scrollview import ScrollView
from kivymd.uix.textfield import MDTextField, MDTextFieldRect
from kivymd.uix.list import MDList, OneLineListItem
from kivymd.uix.widget import MDWidget
from kivymd.uix.anchorlayout import MDAnchorLayout
from kivymd.theming import ThemeManager
from kivymd.uix.gridlayout import MDGridLayout

class FitnessCalcApp(MDApp):
    theme_cls = ThemeManager()
    def build(self):
        self.theme_cls.theme_style='Light'
        self.theme_cls.primary_palette = "Blue"
        self.al = MDAnchorLayout()
        self.bl1 = MDBoxLayout(orientation='vertical', padding=5, spacing=3, size_hint=[.8, .8])
        self.txt1 = MDTextField(input_filter='int', helper_text='Введите Возраст!', required=False,
        helper_text_mode='on_error', hint_text='Введите ваш возраст:', size_hint=[.9,.9])
        self.gl1 = MDGridLayout(rows=2, spacing=15, cols=3, size_hint=[1, 1])
        self.btn1 = MDRoundFlatIconButton(size_hint=[.01, .05], text=' ', on_press = self.sex_choice, id='1')
        self.lbl1 = MDLabel(text='Мужской', font_style='H6', size_hint=[2,2])
        self.btn2 = MDRoundFlatIconButton(size_hint=[.01, .1], text=' ', on_press = self.sex_choice, id='2')
        self.lbl2 = MDLabel(text='Женский', font_style='H6', size_hint=[2,1])
        self.gl1.add_widget( self.btn1)
        self.gl1.add_widget( self.lbl1)
        self.gl1.add_widget( MDWidget())
        self.gl1.add_widget( self.btn2)
        self.gl1.add_widget( self.lbl2)
        self.gl1.add_widget( MDWidget())
        self.gl2 = MDGridLayout(spacing=15, rows=3)
        self.btn3 = MDIconButton( size_hint=[.1, 1], id='3', icon='button02.png', on_press=self.type_of_plans, halign='left', md_bg_color='white', _line_color='white')
        self.btn4 = MDIconButton( size_hint=[.05, 1], id='4', icon='button02.png', on_press=self.type_of_plans)
        self.btn5 = MDIconButton( size_hint=[.1, 1], id='5', icon='button02.png', on_press=self.type_of_plans)
        self.lbl3 = MDLabel(text='Набрать \nмышечную \nмассу', font_style='Caption')
        self.lbl4 = MDLabel(text='Похудение', font_style='Caption')
        self.lbl5 = MDLabel(text='Поддерживать \nвес', font_style='Caption')
        self.gl2.add_widget( self.btn3)
        self.gl2.add_widget( self.lbl3)
        self.gl2.add_widget( self.btn4)
        self.gl2.add_widget( self.lbl4)
        self.gl2.add_widget( self.btn5)   
        self.gl2.add_widget( self.lbl5)
        
        self.bl1.add_widget( self.txt1)
        self.bl1.add_widget( self.gl1)
        self.bl1.add_widget( MDWidget())
        self.bl1.add_widget( self.gl2)
        for i in range( 1):
            self.bl1.add_widget( MDWidget())
        self.al.add_widget( self.bl1)
        return self.al
    def type_of_plans(self, instance):
        if instance.icon != 'button4.png':
            if instance.id == '3':
                if self.btn4.icon and self.btn5.icon != 'button4.png': 
                    self.btn3.icon = 'button4.png'
            elif instance.id == '4':
                if self.btn3.icon and self.btn5.icon != 'button4.png': 
                    self.btn4.icon = 'button4.png'
            elif instance.id == '5':
                if self.btn4.icon and self.btn3.icon != 'button4.png': 
                    self.btn5.icon = 'button4.png'
        else: 
            instance.icon = 'button02.png'
    def sex_choice(self, instance):
        if self.txt1.text == '':
            self.txt1.required=True 
            self.txt1.focus=True 
        elif int(self.txt1.text) >= 130:
            self.txt1.error = True
            self.txt1.focus = True
            self.txt1.helper_text='Введите реальный возраст'
        elif int(self.txt1.text) < 1:
            self.txt1.error = True 
            self.txt1.focus = True
            self.txt1.helper_text='Минимальный возраст: 1'
        elif instance.id == '1':
            if self.btn1.icon == 'galochka.png':
                self.btn1.icon = 'white5.png'
                a = False
            elif self.btn2.icon == '' or self.btn2.icon == 'white5.png':
                self.btn1.icon = 'galochka.png'
                a = False   
            elif self.btn1.icon == 'white5.png':
                self.btn1.icon == 'galochka.png'
                a = False
            else:
                pass
        elif instance.id == '2': 
            if self.btn2.icon == 'galochka.png':
                self.btn2.icon = 'white5.png'
                a = False
            elif self.btn1.icon == '' or self.btn1.icon == 'white5.png':
                self.btn2.icon = 'galochka.png'
                a = False
            elif self.btn2.icon == 'white5.png':
                self.btn2.icon == 'galochka.png'
                a = False
            else:
                pass
app = FitnessCalcApp()
app.run()