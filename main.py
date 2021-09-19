'''
Created on 3/28/2020

@author: dulanj
'''
from pynput.mouse import Listener, Button
import pyscreenshot as ImageGrab
import pytesseract
import pyperclip


class Main():
    def __init__(self, save_image=False):
        self.press_coordinates_captured = False
        self.press_coords = None
        self.release_coords = None
        self.save_image = save_image

        with Listener(on_click=self.on_click) as listener:
            listener.join()

    def on_click(self, x, y, button, pressed):
        if button == Button.middle:
            if pressed:
                if not self.press_coordinates_captured:
                    self.press_coords = (x, y)
                    self.press_coordinates_captured = True
            else:
                if self.press_coordinates_captured:
                    self.release_coords = (x, y)
                    try:
                        im = ImageGrab.grab(bbox=(
                        self.press_coords[0], self.press_coords[1], self.release_coords[0], self.release_coords[1]))
                        filename = ".temp.jpg"
                        if self.save_image:
                            filename = "image_clipped_{}.png".format(self.press_coords[0])
                        im.save(filename)
                        text = pytesseract.image_to_string(im)
                        pyperclip.copy(text)
                        print("Image saved, words: {}".format(text))
                    except ValueError as e:
                        print(e)
                        print("Check the click!!!")
                    finally:
                        self.press_coordinates_captured = False
        else:
            self.press_coordinates_captured = False


if __name__ == "__main__":
    obj = Main()
    obj.main()