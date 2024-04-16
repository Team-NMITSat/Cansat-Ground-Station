import pyqtgraph as pg
import numpy as np
import math

class graph_humidity(pg.PlotItem):
    def __init__(self, parent=None, name=None, labels=None, title='Humidity', viewBox=None, axisItems=None, enableMenu=True, **kargs):
        super().__init__(parent, name, labels, title, viewBox, axisItems, enableMenu, **kargs)
        self.vel_plot = self.plot(pen=(29, 185, 84))
        self.vel_data = np.linspace(0, 0, 30)
        self.ptr = 0

    def update(self, speed):
        self.vel_data[:-1] = self.vel_data[1:]
        self.vel_data[-1] = speed
        self.ptr += 1
        self.vel_plot.setData(self.vel_data)
        self.vel_plot.setPos(self.ptr, 0)
