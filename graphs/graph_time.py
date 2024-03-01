import pyqtgraph as pg
from datetime import datetime

class graph_time(pg.PlotItem):
    
    def __init__(self, parent=None, name=None, labels=None, title='Time Difference', viewBox=None, axisItems=None, enableMenu=True, font=None, **kargs):
        super().__init__(parent, name, labels, title, viewBox, axisItems, enableMenu, **kargs)

        self.hideAxis('bottom')
        self.hideAxis('left')
        self.time_text = pg.TextItem("0:00", anchor=(0.5, 0.5), color="w")
        if font is not None:
            self.time_text.setFont(font)
        self.addItem(self.time_text)
        self.start_time = datetime.now()  # Record the start time when the instance is created

    def update(self):
        current_time = datetime.now()
        time_difference = current_time - self.start_time  # Compute the time difference
        # Format the time difference as minutes:seconds
        self.time_text.setText(str(time_difference.seconds // 60) + ':' + str(time_difference.seconds % 60).zfill(2))
