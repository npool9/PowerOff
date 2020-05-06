from kivy.uix.relativelayout import RelativeLayout
from kivy.app import App
import time
from threading import Timer


class MainPage(RelativeLayout):
    """
    The main page of the application and its various functions
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

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
                self.start_countdown(seconds)
                return seconds
            return seconds
        except ValueError:
            print("Please input numbers in the text boxes.")

    def start_countdown(self, seconds):
        """
        Start a countdown timer for a given number of seconds
        :param seconds: number of seconds chosen by the user until phone turns off
        """
        # TODO: start new thread for stop watch
        print("Turn off phone in", "\033[1m" + str(seconds) + "\033[0m", "seconds.")

    def stop_timer(self):
        """
        Interrupt the stopwatch thread and stop the timer.
        :return: 0 seconds
        """
        # TODO: stop the timer
        print("Stop the timer.")
        app = App.get_running_app()  # get the app's root
        app.root.ids.hours.text = '0'
        app.root.ids.minutes.text = '0'
        return 0
