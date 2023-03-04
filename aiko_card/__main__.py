import pytesseract

from aiko_card.formatting import clear_text
from aiko_card.screenshot import make_screenshot


def main():
    screenshot = make_screenshot()
    screenshot_region = make_screenshot(region=True)
    screenshot_region = screenshot_region.resize(
        (screenshot_region.width * 2, screenshot_region.height * 2)
    )
    sentence = clear_text(pytesseract.image_to_string(screenshot_region))
    print(sentence)


if __name__ == "__main__":
    main()
