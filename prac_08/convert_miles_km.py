"""
CP1404/CP5632 Practical
Kivy GUI program to convert miles to kilometres
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934

class MilesConverterApp(App):
    """ MilesConverterApp is a Kivy App to convert miles to kilometres """
    message = StringProperty()

    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self):
        """ handle calculation for conversion, output result to label """
        try:
            value = float(self.root.ids.input_miles.text)
            self.root.ids.output_miles.text = str(value * MILES_TO_KM)
        except ValueError:
            self.root.ids.output_miles.text = "0.0"

    def handle_increment(self, change):
        """ add or subtract user input, make it into new input """
        try:
            value = float(self.root.ids.input_miles.text) + change
        except ValueError:
            value = "0.0"
        self.root.ids.input_miles.text = str(value)
        self.handle_calculate()

MilesConverterApp().run()