import pyautogui

pyautogui.FAILSAFE = False


class MouseController:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height

    def move(self, x, y):
        pyautogui.moveTo(x, y)

    def click(self):
        pyautogui.click()
