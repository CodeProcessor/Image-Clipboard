'''
Created on 3/28/2020

@author: dulanj
'''
from pynput.mouse import Listener, Button
import pyscreenshot as ImageGrab
import cv2
import pytesseract
from PIL import Image


class Main():
    def __init__(self):
        self.stage_1 = False
        self.press_coords = None
        self.release_coords = None

        with Listener(on_click=self.on_click, on_scroll=self.on_scroll) as listener:
            listener.join()

    def on_click(self, x, y, button, pressed):

        if button == Button.middle:
            stage_1 = False

            if pressed:
                print("pressed")
                if not self.stage_1:
                    self.press_coords = (x, y)
                    self.stage_1 = True
                    print("Stage 1 OK!")
                else:
                    self.release_coords = (x, y)
                    try:
                        im = ImageGrab.grab(bbox=(
                        self.press_coords[0], self.press_coords[1], self.release_coords[0], self.release_coords[1]))
                        filename = "somename_{}.jpg".format(self.press_coords[0])
                        im.save(filename)
                        text = pytesseract.image_to_string(Image.open(filename))
                        print("Image saved, workds: {}".format(text))
                        self.stage_1 = False
                    except ValueError:
                        print("Check the click!!!")

        if button == Button.right:
            self.stage_1 = False
            print("Reset")

        print(button)

    def on_move(self, x, y):
        print ("Mouse moved")


    def on_scroll(self, x, y, dx, dy):
        print ("Mouse scrolled")



if __name__ == "__main__":
    obj = Main()
    obj.main()