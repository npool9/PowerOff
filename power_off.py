from kivy.app import App
from kivy.uix.image import Image
from custom_button_behavior import CustomButtonBehavior
from main_page import MainPage


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
        return MainPage()

    class PowerButton(CustomButtonBehavior, Image):
        """
        The power image as a button
        Defined in the power_off.kv file
        """
        pass


if __name__ == "__main__":
    app = PowerApp()
    app.run()
