import click
import pytesseract
from translatepy import Translator
from translatepy.translators.google import GoogleTranslateV2

from aiko_card.formatting import clear_text
from aiko_card.screenshot import make_screenshot


@click.command()
@click.option(
    "-d",
    "--dest",
    help="Language into which the sentence will be translated",
    required=True,
)
def aiko_card(dest):
    translator = GoogleTranslateV2()
    screenshot = make_screenshot()
    screenshot_region = make_screenshot(region=True)
    screenshot_region = screenshot_region.resize(
        (screenshot_region.width * 2, screenshot_region.height * 2)
    )
    sentence = clear_text(pytesseract.image_to_string(screenshot_region))
    translation = translator.translate(sentence, dest)
    print(sentence, translation)


def main():
    aiko_card()


if __name__ == "__main__":
    main()
