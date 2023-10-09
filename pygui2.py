import sys
import matplotlib
import pandas as pd
matplotlib.use('Qt5Agg')

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import (QApplication, QComboBox, QDialog,
                             QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
                             QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit,
                             QVBoxLayout)


from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure





class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)


        self.canvas = MplCanvas(self, width=50, height=40, dpi=100)
        self.setCentralWidget(self.canvas)
        #self.set

        layout = QVBoxLayout()
        temp_button = QPushButton('temp', self)
        temp_button.clicked.connect(lambda: self.update_plot("temp"))
        layout.addWidget(temp_button)


        light_button = QPushButton('light', self)
        light_button.clicked.connect(lambda: self.update_plot("light"))
        layout.addWidget(light_button)

        #layout.addWidget(self.canvas)

        #layout.addWidget(self.canvas)
        self.setLayout(layout)
        self.setWindowTitle('Sensoru dati')
        self.show()

        # Setup a timer to trigger the redraw by calling update_plot.
        # self.timer = QtCore.QTimer()
        # self.timer.setInterval(100)
        # self.timer.timeout.connect(self.update_plot, 'temp')
        # self.timer.start()



    def update_plot(self, _selected_sensor):
        df = pd.read_csv('iot_telemetry_data.csv')
        # Drop off the first y element, append a new one.
        self.ydata = df[_selected_sensor]
        self.xdata = df['ts']
        self.canvas.axes.cla()  # Clear the canvas.
        self.canvas.axes.plot(self.xdata, self.ydata, 'g')
        # Trigger the canvas to update and redraw.
        self.canvas.draw()


app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
app.exec_()

