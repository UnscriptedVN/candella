# NotificationKit Changes

Candella includes a few improvements to the NotificationKit framework that adds more functionality and modularity to creating notifications with AppKit and NotificationKit screens.

## Notification banner design

Banners in Candella have been moved to the right side of the screen and take up less screen space. They take on the light theme present in the rest of Candella via ScreenKit and use the same fonts. Banners have been positioned so they sit just underneath the top bar in Celeste Shell but also look great in-game.

![Banners in Candella](./images/design/banner.png)

## Creating modular banners {label:new}

Notification banners can be generated automatically using the `CANotificationBanner` class, rather than at call time when invoking `CANotification.send_banner`. This class offers more control over the appearance of the banner and is typically easier to use than the manual mode in previous releases.

To create a banner using `CANotificationBanner`, create an instance of the object with specified details:

```py
banner = CANotificationBanner(
    "Message not sent.", "The message could not be delivered to the recipient.")
```

There are three arguments that must be supplied when creating a new banner:

- message (str): The primary message of the banner.
- details (str): Supporting text for the banner. This could further explain the main message, or provide additional context.
- callback (any): The callback to execute when clicking on the action button. Defaults to `Return('didClickRespond')`.

To invoke this banner in a banner request, pass it as a keyword argument in [`CAApplication.send_banner`](./03-candella-app.md#caapplicationsend_bannertitle-supporting-callbackreturndidclickrespond-labelupdated) and set the mode to `automatic`:

```py
response = CANotification.send_banner(mode='automatic', banner=banner)
```

### Customizing banners

The following attributes are present in `CANotificationBanner` to let developers customize banners:

| Attribute | Type | What it does |
| :-------- | :--- | ------------ |
| message | `str` | The primary message of the banner. |
| details | `str` | The supporting text for the banner. Generally, this explains the primary message or adds additional context. |
| callback | `callable` | A Ren'Py callback function to execute when clicking the action button on the banner. Defaults to `Return('didClickRespond')`. |
| callback_text | `str` | The text for the action button. Defaults to `"Respond"`. |
