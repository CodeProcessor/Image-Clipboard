'''
Created on 3/28/2020

@author: dulanj
'''
import argparse
import logging

import pyperclip
import pyscreenshot as ImageGrab
import pytesseract
from pynput.mouse import Listener, Button


class ImageClipboard:
    def __init__(self, debug=False, save_image=False):
        self.press_coords = None
        self.save_image = save_image
        with Listener(on_click=self.on_click) as listener:
            listener.join()

    def on_click(self, x, y, button, pressed):
        if button == Button.middle:
            if pressed:
                self.press_coords = (x, y)
            else:
                if isinstance(self.press_coords, tuple):
                    release_coords = (x, y)
                    try:
                        im = ImageGrab.grab(
                            bbox=(self.press_coords[0], self.press_coords[1], release_coords[0], release_coords[1]))
                        filename = "../.temp.jpg"
                        if self.save_image:
                            filename = "image_clipped_{}.png".format(self.press_coords[0])
                            logging.info(f"Image saved! - {filename}")
                        im.save(filename)
                        text = pytesseract.image_to_string(im)
                        pyperclip.copy(text)
                        logging.info("clipped: {}".format(text))
                    except ValueError as e:
                        ...
                self.press_coords = None
        else:
            self.press_coords = None


def create_argparse():
    parser = argparse.ArgumentParser()
    parser.add_argument('--debug', help='Enable debug', action='store_true')
    parser.add_argument('--save', help='Enable debug', action='store_true')

    args = parser.parse_args()
    _debug_enabled = args.debug
    _save_enabled = args.save

    if _debug_enabled:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    ImageClipboard(save_image=_save_enabled)


if __name__ == "__main__":
    __save_enabled = True
    ImageClipboard(save_image=__save_enabled)