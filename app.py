from random import randint
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_string('''
<HomeScreen>:
    BoxLayout:
        canvas:
            Color:
                rgba: 0.5, 0.5, 0.5, 1
            Rectangle:
                pos: self.pos
                size: self.size
        orientation: 'vertical'
        Label:
            text: 'Viva'
            size_hint: (None, None)
            size: (500, 100)
            bold: True
            italic: True
            color: (0, 0, 0, 1)
            pos_hint: {'center_x': 0.5, 'top': 1}
            font_size: 100
        Label:
            text: ''
            size: (500, 50)
        Image:
            source: 'nhs.png'
            size_hint: (None, None)
            size: (600, 250)
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            allow_stretch: True
            keep_ratio: False
        Label:
            text: ''
            size: (500, 100)
        Button:
            text: 'Enter Symptoms'
            size_hint: (None, None)
            size: (self.parent.width, 100)
            pos_hint: {'center_x': 0.5, 'center_y': 0.9}
            on_press: 
                root.manager.transition.direction = 'left'
                root.manager.current = 'enter_symptoms'
        Button:
            text: 'List of Symptoms'
            size_hint: (None, None)
            size: (self.parent.width, 100)
            on_press: 
                root.manager.transition.direction = 'left'
                root.manager.current = 'symptoms_list'
                root.on_enter()
        Button:
            text: 'Vital Signs'
            size_hint: (None, None)
            size: (self.parent.width, 100)
            on_press: 
                root.manager.transition.direction = 'left'
                root.manager.current = 'vital_signs'

<EnterSymptoms>:
    FloatLayout:
        canvas:
            Color:
                rgba: .5,.5,.5,1
            Rectangle:
                pos: self.pos
                size: self.size
        Label:
            text: 'Enter Symptoms Below:'
            color: (0, 0, 0, 1)
            size: (500, 100)
            font_size: 40
            bold: True
            pos_hint: {'left': 1, 'center_y': 0.95}
        Label:
            text: 'Date:'
            color: (0, 0, 0, 1)
            size: (500, 100)
            font_size: 30
            pos_hint: {'center_x': 0.08, 'center_y': 0.88}
        TextInput:
            id: date
            multiline: False
            pos_hint: {'left': 1, 'center_y': 0.8}
            size_hint: (1, 0.1)
        Label:
            text: 'Symptoms:'
            color: (0, 0, 0, 1)
            size: (500, 100)
            font_size: 30
            pos_hint: {'center_x': 0.135, 'center_y': 0.7}
        TextInput:
            id: symptoms
            multiline: False
            pos_hint: {'left': 1, 'center_y': 0.57}
            size_hint: (1, 0.2)
        Button:
            text: 'Submit'
            size_hint: (0.5, 0.1)
            pos_hint: {'center_x': 0.5, 'center_y': 0.37}
            on_press:
                root.submit()
                root.manager.transition.direction = 'right'
                root.manager.current = 'home'
        Button:
            text: 'Back'
            size_hint: (0.25, 0.1)
            pos_hint: {'right': 1, 'bottom': 1}
            on_press:
                root.manager.transition.direction = 'right'
                root.manager.current = 'home'

<SymptomsList>:
    on_enter:
        root.on_enter()
    FloatLayout:
        canvas:
            Color:
                rgba: 1, 1, 1, 1
            Rectangle:
                pos: 25, 160
                size: 550, 750
        Label:
            text: 'List of Symptoms:'
            color: (0, 0, 0, 1)
            size: (500, 100)
            font_size: 40
            bold: True
            pos_hint: {'left': 1, 'center_y': 0.95}
        Label:
            id: symptoms_list_label
            text: ''
            color: (0,0,0, 1)
            size: (500, 500)
            font_size: 30
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        Button:
            text: 'Back'
            size_hint: (0.25, 0.1)
            pos_hint: {'right': 1, 'bottom': 1}
            on_press:
                root.on_leave()
                root.manager.transition.direction = 'right'
                root.manager.current = 'home'

<VitalSigns>:
    FloatLayout:
        canvas:
            Color:
                rgba: 1, 1, 1, 1
            Rectangle:
                pos: 25, 750
                size: 550, 100
            Rectangle:
                pos: 25, 550
                size: 550, 100
            Rectangle:
                pos: 25, 350
                size: 550, 100
            Rectangle:
                pos: 25, 150
                size: 550, 100
        Label:
            text: 'Vital Signs:'
            color: (0, 0, 0, 1)
            size: (500, 100)
            font_size: 40
            bold: True
            pos_hint: {'left': 1, 'center_y': 0.95}
        Label:
            text: 'Body Temperature'
            color: (0, 0, 0, 1)
            size: (500, 100)
            font_size: 30
            pos_hint: {'center_x': 0.5, 'center_y': 0.88}
        Label:
            id: body_temperature
            text: ''
            color: (0, 0, 0, 1)
            size: (500, 100)
            font_size: 30
            pos_hint: {'center_x': 0.5, 'center_y': 0.8}
        Label:
            text: 'Pulse Rate'
            color: (0, 0, 0, 1)
            size: (500, 100)
            font_size: 30
            pos_hint: {'center_x': 0.5, 'center_y': 0.68}
        Label:
            id: pulse_rate
            text: ''
            color: (0, 0, 0, 1)
            size: (500, 100)
            font_size: 30
            pos_hint: {'center_x': 0.5, 'center_y': 0.6}
        Label:
            text: 'Respiration Rate'
            color: (0, 0, 0, 1)
            size: (500, 100)
            font_size: 30
            pos_hint: {'center_x': 0.5, 'center_y': 0.48}
        Label:
            id: respiration_rate
            text: ''
            color: (0, 0, 0, 1)
            size: (500, 100)
            font_size: 30
            pos_hint: {'center_x': 0.5, 'center_y': 0.4}
        Label:
            text: 'Blood Pressure'
            color: (0, 0, 0, 1)
            size: (500, 100)
            font_size: 30
            pos_hint: {'center_x': 0.5, 'center_y': 0.28}
        Label:
            id: blood_pressure
            text: ''
            color: (0, 0, 0, 1)
            size: (500, 100)
            font_size: 30
            pos_hint: {'center_x': 0.5, 'center_y': 0.2}
        Button:
            text: 'Back'
            size_hint: (0.25, 0.1)
            pos_hint: {'right': 1, 'bottom': 1}
            on_press:
                root.manager.transition.direction = 'right'
                root.manager.current = 'home'
''')

class HomeScreen(Screen):
    pass

class EnterSymptoms(Screen):
    def submit(self):
        date = self.ids.date.text
        symptoms = self.ids.symptoms.text
        print(f'Date: {date}, Symptoms: {symptoms}')
        self.ids.date.text = ''
        self.ids.symptoms.text = ''
        with open('patient.txt', 'a') as file:
            file.write(f'Date: {date}\nSymptoms: {symptoms}\n')

class SymptomsList(Screen):
    def on_enter(self):
        with open('patient.txt', 'r') as file:
            data = file.readlines()
            filtered_data = []
            for line in data:
                if line.startswith('Date:') or line.startswith('Symptoms:'):
                    filtered_data.append(line.split(':')[1].strip())
                    if line.startswith('Symptoms:'):
                        filtered_data.append('\n')  # Add a new line after every Symptoms line
            text = '\n'.join(filtered_data)
        self.ids.symptoms_list_label.text = str(text)

    def on_leave(self):
        self.ids.symptoms_list_label.text = ''

class VitalSigns(Screen):
    def on_enter(self):
        body_temperature = randint(97, 99)
        pulse_rate = randint(60, 100)
        respiration_rate = randint(12, 20)
        blood_pressure = randint(90, 120)
        self.ids.body_temperature.text = f'{body_temperature} ˚C'
        self.ids.pulse_rate.text = f'{pulse_rate} bpm'
        self.ids.respiration_rate.text = f'{respiration_rate} bpm'
        self.ids.blood_pressure.text = f'{blood_pressure} mmHg'

screen_manager = ScreenManager()
screen_manager.add_widget(HomeScreen(name='home'))
screen_manager.add_widget(EnterSymptoms(name='enter_symptoms'))
screen_manager.add_widget(SymptomsList(name='symptoms_list'))
screen_manager.add_widget(VitalSigns(name='vital_signs'))

class ScenarioApp(App):
    def build(self):
        Window.size = (300, 500)
        Window.clearcolor = (0.5, 0.5, 0.5, 1)
        return screen_manager
    
if __name__ == '__main__':
    app = ScenarioApp()
    app.run()
