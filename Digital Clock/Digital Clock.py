#pip install PyQt5 
#pip install PyQt5-tools
#impprt the following modules

import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QFont, QFontDatabase


class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel( self)  # label for clock display
        self.timer = QTimer(self)  # timer for updating time
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Digital Clock")
        self.setGeometry(600, 400, 300, 100)

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setStyleSheet("font-size:150px; color:green;")


        self.setStyleSheet("background-color:black;")

        # Connect and start timer
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)  # update every 1000 milliseconds (1 second)
        self.update_time()

    def update_time(self):
        # Using lowercase 'ap' for AM/PM format
        current_time = QTime.currentTime().toString("hh:mm:ss ap")
        self.time_label.setText(current_time)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())

