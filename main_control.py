import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import QFile
from PySide2 import QtCore, QtGui
from mainwindow import Ui_MainWindow

import cannon

FILENAME = 'targets.csv'

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.cannon = cannon.Cannon()

        self.timer = QtCore.QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.control_timer)
        self.timer.start()

        self.pan_angle = 0.
        self.tilt_angle = 0.
        self.pan_spd = 0
        self.tilt_spd = 0

        self.targets = {}
        self.target_names = []
        self.read_file(FILENAME)
        self.update_targets_list()

        self.ui.comboBox.currentIndexChanged.connect(self.target_changed)


    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_A:
            self.pan_spd = -1
        if event.key() == QtCore.Qt.Key_D:
            self.pan_spd = 1
        if event.key() == QtCore.Qt.Key_W:
            self.tilt_spd = 1
        if event.key() == QtCore.Qt.Key_S:
            self.tilt_spd = -1
    
    def keyReleaseEvent(self, event):
        if event.key() == QtCore.Qt.Key_A:
            self.pan_spd = 0
        if event.key() == QtCore.Qt.Key_D:
            self.pan_spd = 0
        if event.key() == QtCore.Qt.Key_W:
            self.tilt_spd = 0
        if event.key() == QtCore.Qt.Key_S:
            self.tilt_spd = 0

    def control_timer(self):
        self.pan_angle += self.pan_spd
        self.tilt_angle += self.tilt_spd
        self.cannon.set_pan_tilt(self.pan_angle, self.tilt_angle)
        
        self.ui.current_x.display(self.pan_angle)
        self.ui.current_y.display(self.tilt_angle)

    def read_file(self, name):
        with open(name, 'r') as f:
            for line in f.readlines():
                vals = line.split(',')
                self.target_names.append(vals[0])
                self.targets[vals[0]] = (vals[1], vals[2])

    def update_targets_list(self):
        self.ui.comboBox.clear()
        self.ui.comboBox.addItems(self.target_names)
        try:
            self.ui.target_x.display(self.targets[self.target_names[0]][0])
            self.ui.target_y.display(self.targets[self.target_names[0]][1])
        except Exception:
            pass

    def target_changed(self, index):
        position = self.targets[self.target_names[index]]
        self.ui.target_x.display(position[0])
        self.ui.target_y.display(position[1])
        self.move_to(position[0], position[1])

    def move_to(self, pan, tilt):
        self.cannon.set_pan_tilt(pan, tilt)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())