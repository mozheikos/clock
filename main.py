from datetime import datetime
import sys
from threading import Thread
from time import sleep

from PyQt5 import QtWidgets

from ui import Ui_clock


class Clock(Ui_clock):
    def setupUi(self, _clock):
        super(Clock, self).setupUi(_clock)
        thread = Thread(target=self.clock_work, daemon=True)
        thread.start()
    
    def clock_work(self):
        while True:
            text = datetime.now().strftime('%a %d %b %Y %H:%M:%S')
            date_text, time_text = text.rsplit(' ', 1)
            self.time_screen.setText(time_text)
            self.date_screen.setText(date_text)
            sleep(0.5)

    
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    clock = QtWidgets.QMainWindow()
    ui = Clock()
    ui.setupUi(clock)
    clock.show()
    sys.exit(app.exec_())
    