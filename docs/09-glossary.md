# Glossary

The **Glossary** app for Candella provides a fast and easy way for visual novel developers to define terms used in the game and an intuitive way for users to discover these terms.

## Creating a glossary

The glossary file used in Candella is a JSON file with a single root-level key, `dictionary`. In there, you can define additional words with their respective definitions as a JSON object:

```json
{
    "dictionary": {
        "changeling": "A creature that has the ability to transform into another.",
        "hTML": "Short for hyper-text markup langage, the language that is used to create web pages on the internet."
    }
}
```

If you're including an acronym as a term or need to include uppercase letters, make the first letter lowercase, then use uppercase for the rest. To add spaces to indicate a phrase, use an underscore.

## Displaying the glossary

To display the glossary window with a custom glossary programmatically, use `renpy.show_screen`:

```py
renpy.show_screen(
    "GlossaryAppUIView",
    glossary=glossary.load_glossary("path/to/glossary.json")
)
```

If no arguments are passed in `load_glossary`, the app will default to the built-in glossary.

## Overriding the default glossary

If you need to override the default glossary with your own, you can change the `default_glossary` property of the `glossary` instance. This may be used in scenarios where you want the Glossary app to open your default glossary when the user opens it in a launcher like Celeste Shell.

```py
glossary.default_glossary = "path/to/default_glossary.json"
```