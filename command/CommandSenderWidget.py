from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLineEdit

class CommandSenderWidget(QWidget):
    def __init__(self, send_command_callback, parent=None):
        super().__init__(parent)
        self.initUI(send_command_callback)

    def initUI(self, send_command_callback):
        # Create layout
        layout = QVBoxLayout(self)
        
        # Create the text box for input command
        self.command_input = QLineEdit()
        self.command_input.setStyleSheet("color:rgb(255,255,255); background-color:rgb(50,50,50); font-size:14px;")
        
        # Create the enter button for sending the command
        self.enter_button = QPushButton('Send Command')
        self.enter_button.setStyleSheet("background-color:rgb(29, 185, 84);color:rgb(0,0,0);font-size:14px;")
        
        # Connect the button's clicked signal to the send_command function
        self.enter_button.clicked.connect(lambda: send_command_callback(self.command_input.text()))
        
        # Add widgets to the layout
        layout.addWidget(self.command_input)
        layout.addWidget(self.enter_button)

        # Set the widget's layout
        self.setLayout(layout)

    def clearInput(self):
        """Clears the text input field."""
        self.command_input.clear()

