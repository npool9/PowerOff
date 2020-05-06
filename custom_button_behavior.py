from kivy.properties import OptionProperty, ObjectProperty, NumericProperty, BooleanProperty
from kivy.uix.behaviors import ButtonBehavior


class CustomButtonBehavior(ButtonBehavior):
    state = OptionProperty('normal1', options=('normal1', 'normal2', 'down'))

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.prev_state = None
        self.seconds = 0

    def _do_press(self, *args):
        """
        Override
        """
        self.prev_state = self.state
        self.state = 'down'

    def _do_release(self, *args):
        """
        Override
        """
        if self.prev_state == 'normal1' and self.seconds > 0:
            self.state = 'normal2'
        elif self.prev_state == 'normal2':
            self.state = 'normal1'
        else:
            self.state = self.prev_state
