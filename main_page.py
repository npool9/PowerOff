from kivy.uix.relativelayout import RelativeLayout
from kivy.app import App
from kivy.clock import Clock
from kivy.utils import platform
import time
import subprocess
import math
import dbus
import sys
from kivy.logger import Logger
import os
try:
    from jnius import autoclass
except KeyError:
    os.environ['JDK_HOME'] = "/Library/Java/JavaVirtualMachines/jdk1.8.0_192.jdk/Contents/Home"
    os.environ['JAVA_HOME'] = "/Library/Java/JavaVirtualMachines/jdk1.8.0_192.jdk/Contents/Home"
    from jnius import autoclass


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

        # get root access by OS
        # euid = os.geteuid()
        # if euid != 0:
        #     args = ['su', sys.executable] + sys.argv + [os.environ]
        #     # the next line replaces the currently-running process with the sudo
        #     os.execlpe('sudo', *args)
        #
        # if platform == 'android':
        #     self.python_activity = autoclass("org.kivy.android.PythonActivity").mActivity
        #     self.context = autoclass('android.content.Context')
        #     self.context_compat = autoclass('android.support.v4.content.ContextCompat')

    # def check_permission(self, permission):
    #     """
    #     Check for permissions from the user
    #     :param permission: the permission that we're checking
    #     :return: permission_granted = True or False
    #     """
    #     activity = self.python_activity
    #     permission_status = self.context_compat.checkSelfPermission(activity, permission)
    #
    #     Logger.info(permission_status)
    #     permission_granted = 0 == permission_status
    #     Logger.info("Permission Status: {}".format(permission_granted))
    #     return permission_granted
    #
    # def ask_permission(self, permission):
    #     """
    #     Ask for permission from the user
    #     :param permission: the permission that we're requesting
    #     """
    #     if platform == 'android':
    #         activity = self.python_activity
    #         activity.requestPermissions([permission])

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
        self.time_left -= round(interval)
        stopwatch.text = str(int(self.time_left))
        if self.time_left < 0:
            self.stop_timer()
            print("SHUT DOWN BOI")
            time.sleep(1)
            password = app.root.ids.pw.text
            self.shut_down(password)

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

    def shut_down(self, user_password):
        """
        Shut down the device depending on the device on which the program is being run
        :param user_password: (string) password for shutting down device
        """
        # sys_bus = dbus.SystemBus()
        # ck_srv = sys_bus.get_object('org.freedesktop.ConsoleKit',
        #                             '/org/freedesktop/ConsoleKit/Manager')
        # ck_iface = dbus.Interface(ck_srv, 'org.freedesktop.ConsoleKit.Manager')
        # stop_method = ck_iface.get_dbus_method("Stop")
        # stop_method()
        # ["pmset", "sleepnow"]  # sleep alternative
        # command_dict = {'macosx': ["shutdown", "-h"], 'windows': [], 'android': []}
        # subprocess.run(["pmset", "sleepnow"])
        # iPhone root pw: alpine
        if platform == 'macosx':
            pw = subprocess.Popen(["echo", user_password], stdout=subprocess.PIPE)
            shutdown = subprocess.Popen(['sudo', '-S', 'shutdown', '-h', 'now'], stdin=pw.stdout,
                                        stdout=subprocess.PIPE)
            pw.stdout.close()
            shutdown.communicate()[0]
