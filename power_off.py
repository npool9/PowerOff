from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from main_page import MainPage
import time


class PowerApp(App):
    """
    An application app with all of the main functionality of the fairly simple app.
    """

    def __init__(self, **kwargs):
        """
        Define the attributes of the application object.
        """
        super().__init__(**kwargs)
        self.time = None

        # Image paths
        self.image_path = "Images/"
        self.power_button = "power_button.png"

    def build(self):
        """
        Override the App class's initial build function.
        Here is where the UI functionality is called.
        :return:
        """
        img = Image(source=self.image_path + self.power_button,
                    size_hint=(1, .5),
                    pos_hint={'center_x': .5, 'center_y': .5})
        return MainPage()


if __name__ == "__main__":
    app = PowerApp()
    app.run()
