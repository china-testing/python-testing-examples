import sys
import time
import base64
import serial
import queue
import logging
import threading

from dataclasses import dataclass
from strip_ansi import strip_ansi

from PyQt5 import Qt
from PyQt5.QtCore import QThread, QObject, pyqtSignal
from PyQt5.QtGui import QImage, QPixmap, QFontDatabase 

from PyQt5.QtWidgets import QWidget, QPlainTextEdit, \
QLineEdit, QPushButton, QStatusBar,QLabel, QMainWindow, \
QApplication, QHBoxLayout, QVBoxLayout, QErrorMessage, \
QComboBox, QDoubleSpinBox, QCheckBox

from resources import *

logging.getLogger().setLevel(logging.NOTSET)


@dataclass
class SerialReadMessage:
    message: str
    timestamp: float

@dataclass
class Timer:
    currentTimerWindow: float = -1
    lastSerialInputTime: float = -1


class SerialReader:
    def __init__(self, serial_port, read_Q):
        # Serial port must already be open
        self.serial_port = serial_port
        self.Q = read_Q


    def run(self):
        self.exit = False
        try:
            while True:
                line = self.serial_port.readline()
                if len(line) > 0:
                    self.Q.put(SerialReadMessage(line, time.time()))
                if self.exit:
                    logging.warning('Stopping serial reader thread')
                    break
        except Exception as ex:
            logging.warning('Stopping serial reader thread')
            logging.warning(ex)


    def start_threaded(self):
        logging.info('Starting serial reader thread')
        thread = threading.Thread(target=self.run)
        thread.start()


    def stop(self):
        self.exit = True


class SerialWriter:
    def __init__(self, serial_port, write_Q):
        # Serial port must already be open
        self.serial_port = serial_port
        self.Q = write_Q


    def run(self):
        self.exit = False
        try:
            while True:
                try:
                    if self.exit:
                        logging.warning('Stopping serial writer thread')
                        break
                    line = self.Q.get(block=True, timeout=1)
                except queue.Empty:
                    pass
                else:
                    self.serial_port.write(line)
        except Exception as ex:
            logging.warning('Stopping serial writer thread')
            logging.warning(ex)


    def start_threaded(self):
        logging.info('Starting serial writer thread')
        thread = threading.Thread(target=self.run)
        thread.start()

    def stop(self):
        self.exit = True


class MonitorQ(QThread):
    dataAvailable = pyqtSignal(bytes)

    def __init__(self, Q):
        QThread.__init__(self)
        self.Q = Q

    def run(self):
        while True:
            serialReadMessage = self.Q.get()
            if Timer.currentTimerWindow != -1 and Timer.lastSerialInputTime != -1:
                if serialReadMessage.timestamp <= Timer.lastSerialInputTime + Timer.currentTimerWindow:
                    self.dataAvailable.emit(serialReadMessage.message)
                else:
                    logging.warn('Discarding message, timer window closed')
            else:
                self.dataAvailable.emit(serialReadMessage.message)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        monospacedFont = QFontDatabase.systemFont(QFontDatabase.FixedFont)

        bottombox = QHBoxLayout()
        self.serialPortEdit = QLineEdit()
        self.serialPortEdit.setPlaceholderText("Enter full path to the serial port")
        self.serialPortEdit.returnPressed.connect(self.on_serialportedit_enter_pressed)
        self.serialPortEdit.setFont(monospacedFont)

        self.baudrateComboBox = QComboBox()
        self.std_baudrates = [50, 75, 110, 134, 150, 200, 300, 600, 1200, 1800, 2400, 4800, 9600, 19200, 38400, 57600, 115200]
        self.baudrateComboBox.addItems(map(lambda x: str(x), self.std_baudrates))
        self.baudrateComboBox.setPlaceholderText("Select Baud rate")
        self.baudrateComboBox.setCurrentIndex(-1)
        

        self.connectBtn = QPushButton("Connect")
        self.connectBtn.clicked.connect(self.on_connect_btn_clicked)
        
        self.disconnectBtn = QPushButton("Disconnect")
        self.disconnectBtn.clicked.connect(self.on_disconnect_btn_clicked)
        self.disconnectBtn.setEnabled(False)
        
        bottombox.addWidget(self.serialPortEdit)
        bottombox.addWidget(self.baudrateComboBox)
        bottombox.addWidget(self.connectBtn)
        bottombox.addWidget(self.disconnectBtn)

        mainvbox = QVBoxLayout()
        
        self.serialOutputEdit = QPlainTextEdit()
        self.serialOutputEdit.setReadOnly(True)
        self.serialOutputEdit.setFont(monospacedFont)
        
        self.serialInputEdit = QLineEdit()
        self.serialInputEdit.setPlaceholderText("Enter your data you want to send to the port")
        self.serialInputEdit.setEnabled(False)
        self.serialInputEdit.setFont(monospacedFont)

        mainvbox.addWidget(self.serialOutputEdit)
        mainvbox.addWidget(self.serialInputEdit)
        mainvbox.addLayout(bottombox)

        centralWidget = QWidget(self)
        centralWidget.setLayout(mainvbox)
        self.setCentralWidget(centralWidget)

        self.statusBar = QStatusBar()        

        connectedImage = QImage.fromData(base64.b64decode(connectedImagebase64), "PNG")
        disonnectedImage = QImage.fromData(base64.b64decode(disconnectedImagebase64), "PNG")

        self.connectedImagePixMap = QPixmap.fromImage(connectedImage)
        self.disconnectedImagePixMap = QPixmap.fromImage(disonnectedImage)

        self.connectionStatusLabelIcon = QLabel()
        self.connectionStatusLabelIcon.setPixmap(self.disconnectedImagePixMap)

        self.connectionStatusLabelText = QLabel("Disconnected")

        self.statusBar.addWidget(self.connectionStatusLabelIcon)
        self.statusBar.addWidget(self.connectionStatusLabelText)

        self.timerPushButton = QPushButton("Enable Timer")
        self.timerPushButton.setCheckable(True)
        self.timerPushButton.toggled.connect(self.on_timerPushButton_toggled)

        self.timerWindowDoubleSpinBox = QDoubleSpinBox()
        self.timerWindowDoubleSpinBox.setMinimum(0)
        self.timerWindowDoubleSpinBox.setMaximum(10)
        self.timerWindowDoubleSpinBox.setDecimals(1)
        self.timerWindowDoubleSpinBox.setValue(1)
        self.timerWindowDoubleSpinBox.setSuffix(" s")

        self.clearConsolePushButton = QPushButton("Clear console")
        self.clearConsolePushButton.clicked.connect(self.on_clearConsolePushButton_clicked)

        self.filterStringCheckBox = QCheckBox("Enable Filter")
        self.filterStringCheckBox.stateChanged.connect(self.on_filterStringCheckBox_stateChanged)
        self.filterEnabled = False
        self.filterString = ""

        self.filterStringEdit = QLineEdit()
        self.filterStringEdit.setPlaceholderText("Filter String")
        self.filterStringEdit.setFont(monospacedFont)
        self.filterStringEdit.textEdited.connect(self.on_filterStringEdit_textEdited)
        self.statusBar.addPermanentWidget(self.filterStringCheckBox)
        self.statusBar.addPermanentWidget(self.filterStringEdit)
        self.statusBar.addPermanentWidget(self.clearConsolePushButton)
        self.statusBar.addPermanentWidget(self.timerPushButton)
        self.statusBar.addPermanentWidget(self.timerWindowDoubleSpinBox)


        self.statusBar.layout().setContentsMargins(8, 0, 0, 0)
        self.setStatusBar(self.statusBar)

        self.setGeometry(300, 300, 800, 495)
        self.setWindowTitle('Attify Serial Console')
        self.show()

    def on_filterStringEdit_textEdited(self, text):
        if self.filterStringCheckBox.isChecked():
            self.filterString = text

    def on_filterStringCheckBox_stateChanged(self, state):
        if self.filterStringCheckBox.isChecked():
            self.filterString = self.filterStringEdit.text().strip()
            self.filterEnabled = True
            
        else:
            self.filterEnabled = False


    def on_clearConsolePushButton_clicked(self):
        self.serialOutputEdit.clear()

    def on_timerPushButton_toggled(self, checked):
        self.timerWindowDoubleSpinBox.setEnabled(not checked)

        if checked:
            Timer.currentTimerWindow = self.timerWindowDoubleSpinBox.value()
        else:
            Timer.currentTimerWindow = -1


    def closeEvent(self,event):
        try:
            self.readMonitorQ.quit()
        except:
            pass
        
        try:            
            self.serialReader.stop()
        except:
            pass

        try:
            self.serialWriter.stop()
        except:
            pass

        try:
            self.serial_port.close()
        except:
            pass

        event.accept()


    def on_serialportedit_enter_pressed(self):
        self.on_connect_btn_clicked()


    def on_serialinput_enter_pressed(self):
        cmd = str(self.serialInputEdit.text()).strip()

        if len(cmd) > 0:
            self.serialOutputEdit.appendPlainText('>> ' + cmd)
            cmd = (cmd + '\r\n').encode()
            if Timer.currentTimerWindow != -1:
                Timer.lastSerialInputTime = time.time()
            self.write_Q.put(cmd)
            self.serialInputEdit.clear()            


    def on_connect_btn_clicked(self):
        serial_port_txt = self.serialPortEdit.text()
        if len(serial_port_txt) > 0:
            index = self.baudrateComboBox.currentIndex()
            if index == -1:
                error_dialog = QErrorMessage(self)
                error_dialog.setModal(True)                
                error_dialog.showMessage("Please select a baud rate")
            else:
                baud_rate = self.std_baudrates[index]
                try:
                    self.serial_port = serial.Serial(serial_port_txt, timeout=1, baudrate=baud_rate)
                except Exception as ex:
                    error_dialog = QErrorMessage(self)
                    error_dialog.setModal(True)                
                    error_dialog.showMessage(str(ex))
                else:
                    self.connectBtn.setEnabled(False)
                    self.disconnectBtn.setEnabled(True)
                    self.serialInputEdit.setEnabled(True)
                    self.connectionStatusLabelText.setText("Connected")
                    self.connectionStatusLabelIcon.setPixmap(self.connectedImagePixMap)
                    self.baudrateComboBox.setEnabled(False)

                    self.start_reader()
                    self.start_writer()


    def write_to_Serial_Output_Edit(self, data):
        cleaned_text = strip_ansi(data.decode('ascii')).strip()
        if (self.filterEnabled and self.filterString not in cleaned_text) or not self.filterEnabled:
            self.serialOutputEdit.appendPlainText(cleaned_text)



    def start_reader(self):
        self.read_Q = queue.Queue()
        self.serialReader = SerialReader(self.serial_port, self.read_Q)
        self.serialReader.start_threaded()

        self.readMonitorQ = MonitorQ(self.read_Q)
        self.readMonitorQ.dataAvailable.connect(self.write_to_Serial_Output_Edit)
        self.readMonitorQ.start()
        

    def start_writer(self):
        self.write_Q = queue.Queue()
        self.serialWriter = SerialWriter(self.serial_port, self.write_Q)
        self.serialWriter.start_threaded()

        self.serialInputEdit.returnPressed.connect(self.on_serialinput_enter_pressed)


    def on_disconnect_btn_clicked(self):
        self.connectBtn.setEnabled(True)
        self.disconnectBtn.setEnabled(False)
        self.serialInputEdit.setEnabled(False)
        self.connectionStatusLabelText.setText("Disconnected")
        self.connectionStatusLabelIcon.setPixmap(self.disconnectedImagePixMap)
        self.serialInputEdit.returnPressed.disconnect(self.on_serialinput_enter_pressed)
        self.baudrateComboBox.setEnabled(True)
        self.readMonitorQ.quit()
        self.serialReader.stop()
        self.serialWriter.stop()
        self.serial_port.close()


def main():
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
#/dev/pts/5
