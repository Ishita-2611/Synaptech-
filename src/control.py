from pynput.keyboard import Controller
from pynput.mouse import Controller as MouseController

keyboard = Controller()
mouse = MouseController()

def control_laptop(action):
    if action == "left":
        keyboard.press('left')
        keyboard.release('left')
    elif action == "right":
        keyboard.press('right')
        keyboard.release('right')
    elif action == "click":
        mouse.click(Button.left, 1)

if __name__ == "__main__":
    control_laptop("left")  # Test function
