# Design and branding

Candella includes utilities and modules that help ensure the system's design language is followed, as well as provide branding images.

## Design

Candella, in large part, follows the Suru design guidelines and is commonly seen in the icons and font (Ubuntu). The `CADesign` module contains some utilities to help facilitate following the design language.

### `get_app_mask_frame()`

Returns a Frame object with a mask of the app's general shape.

### `get_app_mask(icon, size)`

Returns an AlphaMask displayable with the app's general shape masked on to the specified `icon` with a size of `size x size` pixels.

## Branding

The `Branding` directory inside of the `System/Library` directory contains logomarks and sprites that can be used throughout Candella. Please, do not use these images to represent your app or service.

![Logomark](/images/branding/logomark.png)
<small>

*The logomark is best used on a dark background.

</small>

| | |
| - | - |
| ![Logo sprite](/images/branding/sprite.png) | ![Alternate logo sprite](/images/branding/sprite_alt.png) |

Note that, for fonts, the Ubuntu font is used.
