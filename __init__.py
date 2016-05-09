"""
Bar widget
===========

The :class:`Bar` represents the percentage value from 0-100 range
as colored rectangle, known from f.e. statistics graphs/charts.

Bar widget has no interactive elements and is a display-only widget.

Bar widget supports animating the value changes
with the power of :class:`~kivy.animation.Animation` class.
The color of the bar and the background also can be customized.

Bar widget works with all orientations: the value can be drawn
from left, top, right or bottom.

It can be used from both Python and KV.

.. code-block:: python

    b = Bar()
    b.value = 20
    # bar will be coloured in 10%
    b.value = 85
    # bar will be coloured in 85%

.. code-block:: kv

    BoxLayout:

        Bar:
            value: 85
            orientation: 'lr' # horizontal bar

        Bar:
            value: 10
            orientation: 'bt' # vertical bar

Value change could be animated.
Bar supports all :class:`~kivy.animation.Animation` class animation types.
Animation could be disabled by setting :attr:`animated` to False.
"""

from kivy.uix.widget import Widget
from kivy.properties import (
    NumericProperty,
    OptionProperty,
    ListProperty,
    BooleanProperty,
    StringProperty,
    BoundedNumericProperty
)
from kivy.animation import Animation
from kivy.lang import Builder

Builder.load_string('''
<Bar>:
    canvas:
        Color:
            rgba: root.background_color
        Rectangle:
            pos: root.pos
            size: root.size
        Color:
            rgba: root.color
        Rectangle:
            pos: self.pos if self.orientation in ('lr', 'bt') else (self.right - self.width*self._value/100., self.y) if root.orientation == 'rl' else (self.x, self.top - self.height*self._value/100.)
            size: (self.width*self._value/100., self.height) if root.orientation in ('lr', 'rl') else (self.width, self.height*self._value/100.)
''')


class Bar(Widget):
    """Bar representing the value from 0-100 percent range."""

    value = BoundedNumericProperty(0., min=0., max=100.)
    """Value that bar represents.

    Accepts values in 0.-100. range (percentage).

    :attr: `value` is a :class:`~kivy.properties.BoundedNumericProperty`
    and defaults to 0.
    """

    orientation = OptionProperty('bt', options=('lr', 'rl', 'bt', 'tb'))
    """Orientation of the value drawing.

    Can take one of the 4 values:
        `lr`: from left to right
        `rl`: from right to left
        `bt`: from bottom to top
        `tb`: from top to bottom

    :attr:`orientation` is a :class:`~kivy.properties.OptionProperty`
    and defaults to 'bt'.
    """

    color = ListProperty([1, 1, 1, 1])
    """Color of the value drawing.

    :attr:`color` is a :class:`~kivy.properties.ListProperty`
    and defaults to [1, 1, 1, 1].
    """

    background_color = ListProperty([0, 0, 0, 1])
    """Color of the background.

    :attr:`background_color` is a :class:`~kivy.properties.ListProperty`
    and defaults to [0, 0, 0, 1].
    """

    animated = BooleanProperty(True)
    """Indicates if the bar should be animated.

    :attr:`animated` is a :class:`~kivy.properties.BooleanProperty`
    and defaults to True.
    """

    anim_type = StringProperty('linear')
    """Type of the value update animation.

    Check :class:`~kivy.animation.Animation` for more details.

    :attr:`anim_type` is a :class:`~kivy.properties.StringProperty`
    and defaults to 'linear'.
    """

    anim_duration = NumericProperty(.5)
    """Duration of the value update animation.

    :attr: `value` is a :class:`~kivy.properties.NumericProperty`
    and defaults to .5.
    """

    # internal

    _value = NumericProperty(0.0)
    """Value used directly for drawing on the canvas."""

    _anim = None
    """Animation object used to animate the value change."""

    def on_value(self, instance, value):
        """Handler called when :attr:`value` value changes."""
        if self.animated:
            if self._anim:
                Animation.cancel_all(self)
                self._anim = None
            a = Animation(_value=value, t=self.anim_type, d=self.anim_duration)
            a.start(self)
            self._anim = a
        else:
            self._value = value


if __name__ == '__main__':
    from kivy.base import runTouchApp
    from kivy.clock import Clock
    import random

    kv = Builder.load_string('''
BoxLayout:

    Bar:
        id: bar
        value: slider.value
        animated: tbutton.state == 'down'
        anim_duration: 1
        color: 1, 0.2, 0.3, 1
        orientation: spinner.text
        anim_type: spinner2.text
        on_value: print('Value changed to: {}'.format(self.value))

    BoxLayout:
        orientation: 'vertical'
        size_hint: None, 1
        width: '200dp'

        Label:
            text: 'Value: {}'.format(slider.value)

        Slider:
            id: slider
            value: 30
            max: 100
            min: 0

        ToggleButton:
            text: 'Animated'
            id: tbutton
            state: 'down'

        Spinner:
            id: spinner
            values: 'bt', 'tb', 'lr', 'rl'
            text: 'bt'

        Spinner:
            id: spinner2
            text: 'linear'
            values: 'linear', 'in_back', 'in_out_expo', 'out_elastic'

    ''')
    runTouchApp(kv)
