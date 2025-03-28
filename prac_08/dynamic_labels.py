"""
Kivy example for CP1404/CP5632, IT@JCU
Dynamically create labels based on content on list
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

class DynamicLabelsApp(App):
    """Main program - Kivy app to demo dynamic label creation."""
    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.names = ['Claire', 'Rebecca', 'Sherry']

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create labels from data and add them to the GUI."""
        for name in self.names:
            temp_label = Label(text=name, color=(0, 1, 1, 1))
            temp_label.background_colour = (1, 0.5, 0.5, 1)
            self.root.ids.main.add_widget(temp_label)

DynamicLabelsApp().run()
