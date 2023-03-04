import pytesseract

from aiko_card.formatting import clear_text
from aiko_card.screenshot import make_screenshot


def main():
    screenshot = make_screenshot()
    screenshot_region = make_screenshot(region=True)


if __name__ == "__main__":
    main()
