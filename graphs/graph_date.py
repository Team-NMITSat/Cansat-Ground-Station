import pyqtgraph as pg


class graph_date(pg.PlotItem):
        
    def __init__(self, parent=None, name=None, labels=None, title='Date', viewBox=None, axisItems=None, enableMenu=True, font = None,**kargs):
        super().__init__(parent, name, labels, title, viewBox, axisItems, enableMenu, **kargs)

        self.hideAxis('bottom')
        self.hideAxis('left')
        self.time_text = pg.TextItem("test", anchor=(0.5, 0.5), color="w")
        if font != None:
            self.time_text.setFont(font)
        self.addItem(self.time_text)


    def update(self, value):
        self.time_text.setText('')
        self.time_text.setText(str(value))