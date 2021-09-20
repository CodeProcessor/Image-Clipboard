'''
Created on 3/28/2020

@author: dulanj
'''
import argparse
import logging
import os

import pyperclip
import pyscreenshot as ImageGrab
import pytesseract
from pynput.mouse import Listener, Button


class ImageClipboard:
    """
    This is the main class responsible for getting the work done
    """
    def __init__(self, save_image=False):
        """
        Initializing couple of self variables
        Start the mouse click listner
        :param save_image: Boolean value to whether save all the images or not
        """
        self.press_coords = None
        self.save_image = save_image
        with Listener(on_click=self.on_click) as listener:
            listener.join()

    def on_click(self, x, y, button, pressed):
        """
        This function will trigger whenever there is a mouse click
        :param x: x mouse coordinate
        :param y: y mouse coordinate
        :param button: which button pressed
        :param pressed: button pressed or released
        :return: None
        """
        if button == Button.middle:
            if pressed:
                self.press_coords = (x, y)
                logging.debug(f"Middle Button Pressed | Coordinates {self.press_coords}")
            else:
                if isinstance(self.press_coords, tuple):
                    release_coords = (x, y)
                    logging.debug(f"Middle Button Released | Coordinates {release_coords}")
                    try:
                        im = ImageGrab.grab(
                            bbox=(self.press_coords[0], self.press_coords[1], release_coords[0], release_coords[1]))
                        _filename = ".temp.jpg"
                        if self.save_image:
                            _filename = "image_clipped_{}.png".format(self.press_coords[0])
                            logging.info(f"Image saved! - {_filename}")
                        _filename_full = os.path.join(os.path.expanduser('~'), _filename)
                        im.save(_filename)
                        logging.debug("Image saved! |{}".format(_filename))
                        text = pytesseract.image_to_string(im).strip()
                        pyperclip.copy(text)
                        logging.info("clipped:{}".format(text))
                    except ValueError as e:
                        logging.debug(f"Invalid coordinates to capture an image")
                self.press_coords = None
        else:
            self.press_coords = None


def create_argparse():
    """
    Create the argparse to take the arguments
    --debug will save all the information
    --save will save all the images that captured
    :return: None
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--debug', help='Enable debug logs', action='store_true')
    parser.add_argument('--save', help='Enable to save all the captured images', action='store_true')

    args = parser.parse_args()
    _debug_enabled = args.debug
    _save_enabled = args.save

    if _debug_enabled:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)
    _msg = "Image clip started!"
    _msg += " | Image save is enabled." if _save_enabled else ""
    logging.info(_msg)
    try:
        ImageClipboard(save_image=_save_enabled)
    except KeyboardInterrupt:
        logging.info("Image clip stopped!")
    except Exception as e:
        url = "https://github.com/CodeProcessor/Image-Clipboard/issues"
        logging.exception(f"Exception fired - \nPlease create an issue in {url} and help down to track it")
    finally:
        git_link = "https://github.com/CodeProcessor"
        logging.info("Thank you for using image clipper")
        logging.info(f"Follow me! - {git_link}")


if __name__ == "__main__":
    __save_enabled = True
    logging.basicConfig(level=logging.INFO)
    ImageClipboard(save_image=__save_enabled)
