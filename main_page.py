from kivy.uix.relativelayout import RelativeLayout
from kivy.app import App
import time
from threading import Timer


class MainPage(RelativeLayout):
    """
    The main page of the application and its various functions
    """

    def calculate_time(self):
        """
        Read the text inputs in the hours text box and minutes text box, and calculate the seconds to wait until phone
        is powered off.
        :return: seconds (int)
        """
        try:
            app = App.get_running_app()  # get the app's root
            hours = int(app.root.ids.hours.text)
            minutes = int(app.root.ids.minutes.text)
            seconds = hours * 60 * 60 + minutes * 60
            if seconds == 0:
                print("Please input a time greater than 0.")
            else:
                print("Seconds until phone will turn off:", seconds)
                self.start_countdown(seconds)
            return seconds
        except ValueError:
            print("Please input numbers in the text boxes.")

    def start_countdown(self, seconds):
        """
        Start a countdown timer for a given number of seconds
        :param seconds: number of seconds chosen by the user until phone turns off
        """
        # start new thread for stop watch
