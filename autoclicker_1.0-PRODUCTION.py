import time
import threading
from pynput import mouse
from pynput.mouse import Button, Controller, Listener

mouse = Controller()
button = Button.left
start_stop_key = Button.x2
stop_key = Button.middle
delay = 0.001

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

click_thread = ClickMouse(delay, button)
click_thread.start()

def on_click(x, y, key, but):
    """
    print(x)
    print(y)
    print(key)
    print(but)
    """
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

# Collect events until released
with Listener(on_click=on_click) as listener:
        listener.join()