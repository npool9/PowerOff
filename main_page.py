from kivy.uix.relativelayout import RelativeLayout
from kivy.app import App
import os
from kivy.clock import Clock


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

    # def start_countdown(self):
    #     """
    #     Start a countdown timer for a given number of seconds
    #     """
    #     # TODO: start new thread for stop watch
    #     print("Turn off phone in", "\033[1m" + str(self.time_left) + "\033[0m", "seconds.")
    #     interval = 1.0
    #     st = ShutdownTimer(interval, self.count_down, interval)
    #     # try:
    #     #     time.sleep(self.time_left)  # your long-running job goes here...
    #     if self.time_left <= 0:
    #         st.stop()  # better in a try/finally block to make sure the program ends!

    def count_down(self, interval):
        """
        Count down (stopwatch) from a given number of seconds
        :param interval: the delta time
        :return: remaining seconds
        """
        self.time_left -= interval
        if self.time_left < 0:
            self.stop_timer()
            print("SHUT DOWN BOI")
            # os.system("shutdown /s /t 1")

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
        return 0
