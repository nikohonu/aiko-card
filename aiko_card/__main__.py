import click
import pytesseract
from translatepy.translators.google import GoogleTranslateV2

from aiko_card.anki import add_card
from aiko_card.formatting import clear_text
from aiko_card.screenshot import make_screenshot


@click.command()
@click.option(
    "-d",
    "--deck",
    help="Designated Anki deck",
    required=True,
)
@click.option(
    "-m",
    "--model",
    help="Model of Anki card",
    required=True,
)
@click.option(
    "-s",
    "--sentence",
    "sentence_field",
    default="Sentence",
    help="Name of sentence field",
)
@click.option(
    "-t",
    "--t",
    "translation_field",
    default="Translation",
    help="Name of translation field",
)
@click.option(
    "-p",
    "--p",
    "picture_field",
    default="Picture",
    help="Name of translation field",
)
@click.option(
    "-l",
    "--lang",
    help="Language into which the sentence will be translated",
    required=True,
)
def aiko_card(deck, model, sentence_field, translation_field, picture_field, lang):
    translator = GoogleTranslateV2()
    screenshot = make_screenshot()
    screenshot.thumbnail((screenshot.width / 4.0, screenshot.height / 4.0))
    screenshot_region = make_screenshot(region=True)
    screenshot_region = screenshot_region.resize(
        (screenshot_region.width * 2, screenshot_region.height * 2)
    )
    sentence = clear_text(pytesseract.image_to_string(screenshot_region))
    translation = translator.translate(sentence, lang).result
    add_card(
        deck,
        model,
        sentence_field,
        translation_field,
        picture_field,
        sentence,
        translation,
        screenshot,
    )


def main():
    aiko_card()


if __name__ == "__main__":
    main()
