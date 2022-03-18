import time
import threading
from pynput import mouse
from pynput.mouse import Button, Controller, Listener, Events

mouse = Controller()
button = Button.left
start_stop_key = Button.x2
stop_key = Button.middle
delay = 0.001
run = True


class ClickMouse(threading.Thread):

    # delay and button is passed in class
    # to check execution of auto-clicker
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    # method to check and run loop until 
    # it is true another loop will check 
    # if it is set to true or not, 
    # for mouse click it set to button 
    # and delay.
    def run(self):
        while self.program_running:
            while self.running:
                mouse.click(self.button)
                time.sleep(self.delay)
            time.sleep(0.1)


# click_thread = ClickMouse(delay, button)
# click_thread.start()

def on_click(x, y, key, but):
    """
    print(x)
    print(y)
    print(key)
    print(but)
    """
    print('x = {}, y = {}, key = {}, button = {}'.format(x, y, key, but))
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()
    # here exit method is called and when 
    # key is pressed it terminates auto clicker
    elif key == stop_key:
        click_thread.exit()
        listener.stop()


try:
    while run:
        exe = str(input("Please select from the following...\n     A - Activate Program\n     Q - Quit\nChoose: "))
        if exe.upper() == "A":
            print("AutoClicker9000 running....")
            click_thread = ClickMouse(delay, button)
            click_thread.start()
            print(click_thread)
            # three lines below this are still a mystery to me. I kind of understand what's happening but not getting
            # the full picture yet (3/17/22)
            with Listener(on_click=on_click) as listener:
                print(listener)
                listener.join()
        elif exe.upper() == "Q":
            run = False
            click_thread.exit()
        else:
            print("Invalid input please try again and choose from the choices provided.")
except Exception as error:
    print(error)
