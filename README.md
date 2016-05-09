#Bar widget

`Bar` represents the percentage value from 0-100 range
as colored rectangle, known from f.e. statistics graphs/charts.

`Bar` widget has no interactive elements and is a display-only widget.

Bar widget supports animating the value changes
with the power of [`kivy.animation.Animation`](https://kivy.org/docs/api-kivy.animation.html) class. Bar supports all [`kivy.animation.Animation`](https://kivy.org/docs/api-kivy.animation.html) class animation types. Animation could be disabled by setting `animated` to False. The color of the bar and the background also can be customized.

Bar widget works with all orientations: the value can be drawn
from left, top, right or bottom.

It can be used from both Python...

```python
b = Bar()
b.value = 20
# bar will be coloured in 10%
b.value = 85
# bar will be coloured in 85%
```

...and KV.

```python
BoxLayout:
    Bar:
        value: 85
        orientation: 'lr' # horizontal bar
    Bar:
        value: 10
        orientation: 'bt' # vertical bar
```
