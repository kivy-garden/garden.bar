#Bar widget

`Bar` represents the percentage value from 0-100 range
as colored rectangle, known from f.e. statistics graphs/charts. It has no interactive elements and is a display-only widget.

Bar widget supports animating the value changes
with the power of [`kivy.animation.Animation`](https://kivy.org/docs/api-kivy.animation.html) class. Bar supports all [`kivy.animation.AnimationTransition`](https://kivy.org/docs/api-kivy.animation.html#kivy.animation.AnimationTransition) class animation types. Animation could be disabled by setting `animated` to `False`. The color of the bar and the background also can be customized.

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

## API

`Bar` class provides the set of properties, which changed provide a specific widget behaviour. These properties are a standard [Kivy properties](https://kivy.org/docs/api-kivy.properties.html), so it means they are event driven and bindable.

```
value
```

Value that bar represents. Accepts values in 0.-100. range (percentage).`value` is a [`kivy.properties.BoundedNumericProperty`](https://kivy.org/docs/api-kivy.properties.html#kivy.properties.BoundedNumericProperty) and defaults to `0`.

```
orientation
```

Orientation of the value drawing. It can take one of the 4 values:

    `lr` from left to right
    
    
    `rl` from right to left
    
    
    `bt` from bottom to top
    
    
    `tb` from top to bottom

`orientation` is a [`kivy.properties.OptionProperty`](https://kivy.org/docs/api-kivy.properties.html#kivy.properties.OptionProperty) and defaults to `bt`.
