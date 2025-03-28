"""
CP1404/CP5632 Practical
Kivy GUI program to greet name and clear text
"""

from kivy.app import App
from kivy.lang import Builder

class BoxLayoutDemo(App):
    """BoxLayoutDemoApp is a Kivy App to enter, greet, clear name"""
    def build(self):
        """build the Kivy app from the kv file"""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout_demo.kv')
        return self.root

    def handle_greet(self):
        """say hello with user input when "greet" button pressed"""
        print('greet')
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def handle_clear(self):
        """clear all text of user input and output when "clear" button pressed"""
        self.root.ids.input_name.text = ''
        self.root.ids.output_label.text = ''


BoxLayoutDemo().run()
