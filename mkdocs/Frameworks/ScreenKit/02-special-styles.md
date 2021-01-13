# Special ScreenKit Styles

Not all ScreenKit elements can be easily inherited via the style prefix. To accommodate for this, ScreenKit also includes some special styles that must be applied to an interface element specifically.

## Text Buttons

The following styles apply to text buttons (`textbutton`). These styles can also be used as a style prefix when in a `hbox` or a `vbox`. For example, both are acceptable:

```
textbutton "Continue" action NullAction():
    style "ASInterfacePushButton"

hbox:
    style_prefix "ASInterfacePushButton"
    textbutton "Cancel" action NullAction()
    textbutton "Continue" action NullAction()
```

### `ASInterfacePushButton`
The base style for a push button.

### `ASInterfaceCheckbox`
The base style for a checkbox.

### `ASInterfaceRadio`
The base style for a radio button.

## Scrollable Content
The following styles apply to scrollable areas where a scrollbar is present. Generally, this is called as a style prefix rather than the style itself.

### `ASInterfaceScrollbar`
The base style for a scrollable area.

- Used with `viewport`.
- Can be used as a style prefix.