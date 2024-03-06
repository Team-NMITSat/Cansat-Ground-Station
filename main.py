import sys
from pyqtgraph.Qt import QtGui, QtCore, QtWidgets
import pyqtgraph as pg
from communication import Communication
from dataBase import data_base
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QPushButton, QLineEdit
from graphs.graph_acceleration import graph_acceleration
from graphs.graph_altitude import graph_altitude
from graphs.graph_battery import graph_battery
from graphs.graph_free_fall import graph_free_fall
from graphs.graph_gyro import graph_gyro
from graphs.graph_pressure import graph_pressure
from graphs.graph_speed import graph_speed
from graphs.graph_temperature import graph_temperature
from graphs.graph_time import graph_time
from graphs.graph_lat import graph_lat
from graphs.graph_long import graph_long
from graphs.graph_date import graph_date
from command.CommandSenderWidget import CommandSenderWidget

pg.setConfigOption('background', (33, 33, 33))
pg.setConfigOption('foreground', (197, 198, 199))
# Interface variables
app = QtWidgets.QApplication(sys.argv)
view = pg.GraphicsView()
Layout = pg.GraphicsLayout()
view.setCentralItem(Layout)
view.show()
view.setWindowTitle('Flight monitoring')
view.resize(1200, 700)

# declare object for serial Communication
ser = Communication()
# declare object for storage in CSV
data_base = data_base()
# Fonts for text items
font = QtGui.QFont()
font.setPixelSize(45)

font0 = QtGui.QFont()
font0.setPixelSize(30)

# buttons style
style = "background-color:rgb(29, 185, 84);color:rgb(0,0,0);font-size:14px;"


# Declare graphs
# Button 1
proxy = QtWidgets.QGraphicsProxyWidget()
save_button = QtWidgets.QPushButton('Start storage')
save_button.setStyleSheet(style)
save_button.clicked.connect(data_base.start)
proxy.setWidget(save_button)

# Button 2
proxy2 = QtWidgets.QGraphicsProxyWidget()
end_save_button = QtWidgets.QPushButton('Stop storage')
end_save_button.setStyleSheet(style)
end_save_button.clicked.connect(data_base.stop)
proxy2.setWidget(end_save_button)

# Altitude graph
altitude = graph_altitude()
# Speed graph
speed = graph_speed()
# Acceleration graph
acceleration = graph_acceleration()
# Gyro graph
gyro = graph_gyro()
# Pressure Graph
pressure = graph_pressure()
# Temperature graph
temperature = graph_temperature()
# Time graph
time = graph_time(font=font)
# Battery graph 
battery = graph_battery(font=font)
# Free fall graph
free_fall = graph_free_fall(font=font)

lat = graph_lat(font=font0)

long  = graph_long(font=font0)

date = graph_date(font=font0)

## Setting the graphs in the layout 
# Title at top
text = """
Team NMITSat
"""
Layout.addLabel(text, col=1, colspan=21)
Layout.nextRow()

# Put vertical label on left side
Layout.addLabel('labs',
                angle=-90, rowspan=3)
                
Layout.nextRow()

lb = Layout.addLayout(colspan=21)
lb.addItem(proxy)
lb.nextCol()
lb.addItem(proxy2)

Layout.nextRow()

l1 = Layout.addLayout(colspan=20, rowspan=2)
l11 = l1.addLayout(rowspan=1, border=(83, 83, 83))

# Altitude, speed
l11.addItem(altitude)
l11.addItem(speed)
l1.nextRow()

# Acceleration, gyro, pressure, temperature
l12 = l1.addLayout(rowspan=1, border=(83, 83, 83))
l12.addItem(acceleration)
l12.addItem(gyro)
l12.addItem(pressure)
l12.addItem(temperature)

# Time, battery and free fall graphs
l2 = Layout.addLayout(border=(83, 83, 83))
l2.addItem(date)
l2.nextRow()
l2.addItem(time)
l2.nextRow()
l2.addItem(battery)
l2.nextRow()
l2.addItem(free_fall)
l2.nextRow()
l2.addItem(lat)
l2.nextRow()
l2.addItem(long)

def send_command(command):
    ser.sendData(command)
    print(f"Command to send: {command}")
    command_sender_widget.clearInput()  # Clear the input after sending the command

command_sender_widget = CommandSenderWidget(send_command)
proxy = QtWidgets.QGraphicsProxyWidget()
proxy.setWidget(command_sender_widget)
l2.nextRow()
Layout.addItem(proxy)

def update():
    try:
        value_chain = []
        value_chain = ser.getData()
        #value_chain = [0, 1,2,3,4,5,6,7,8,9,10,11,12,13]
        acceleration.update(value_chain[0], value_chain[1], value_chain[2])
        altitude.update(value_chain[3])
        free_fall.update(value_chain[3])
        temperature.update(value_chain[4])
        pressure.update(value_chain[5])
        gyro.update(value_chain[6], value_chain[7], value_chain[8])
        lat.update(value_chain[9])
        long.update(value_chain[10])
        date.update(value_chain[11])
        battery.update(value_chain[12])
        speed.update(value_chain[13])
        time.update()
        data_base.guardar(value_chain)
    except IndexError:
        print('starting, please wait a moment')


if(ser.isOpen()) or (ser.dummyMode()):
    timer = pg.QtCore.QTimer()
    timer.timeout.connect(update)
    timer.start(500)
else:
    print("something is wrong with the update call")
# Start Qt event loop unless running in interactive mode.

if __name__ == '__main__':
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtWidgets.QApplication.instance().exec_()
