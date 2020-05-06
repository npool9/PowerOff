from kivy.uix.relativelayout import RelativeLayout
from kivy.app import App
import os
from kivy.clock import Clock
import dbus


class MainPage(RelativeLayout):
    """
    The main page of the application and its various functions
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.timer_state = None
        self.time_left = None
        self.interval = 1
        self.timer_event = None

    def calculate_time(self):
        """
        Read the text inputs in the hours text box and minutes text box, and calculate the seconds to wait until phone
        is powered off.
        :return: seconds (float)
        """
        try:
            app = App.get_running_app()  # get the app's root
            hours = int(app.root.ids.hours.text)
            minutes = int(app.root.ids.minutes.text)
            seconds = int(app.root.ids.seconds.text)
            seconds = hours * 60 * 60 + minutes * 60 + seconds
            if seconds == 0:
                self.time_left = None
                print("Please input a time greater than 0.")
            else:
                self.time_left = seconds
                self.timer_event = Clock.schedule_interval(self.count_down, self.interval)
            return seconds
        except ValueError:
            print("Please input numbers in the text boxes.")

    def count_down(self, interval):
        """
        Count down (stopwatch) from a given number of seconds
        :param interval: the delta time
        :return: remaining seconds
        """
        app = App.get_running_app()  # get app's root
        stopwatch = app.root.ids.stopwatch
        stopwatch.text = str(int(self.time_left))
        self.time_left -= interval
        if self.time_left < 0:
            self.stop_timer()
            print("SHUT DOWN BOI")
            os.system("shutdown /s /t 1")

    def stop_timer(self):
        """
        Interrupt the stopwatch thread and stop the timer.
        :return: 0 seconds
        """
        # TODO: stop the timer
        print("Stop the timer.")
        self.timer_event.cancel()
        app = App.get_running_app()  # get the app's root
        app.root.ids.power_button.state = 'normal1'  # reset state
        app.root.ids.hours.text = '0'
        app.root.ids.minutes.text = '0'
        app.root.ids.seconds.text = '0'
        app.root.ids.stopwatch.text = '0'
        return 0

