import random
import serial
import serial.tools.list_ports


class Communication:
    baudrate = ''
    portName = ''
    dummyPlug = False
    ports = serial.tools.list_ports.comports()
    ser = serial.Serial()

    def __init__(self):
        self.baudrate = 115200
        print("the available ports are (if none appear, press any letter): ")
        for port in sorted(self.ports):
            # obtener la lista de puetos: https://stackoverflow.com/a/52809180
            print(("{}".format(port)))
        self.portName = input("write serial port name (ex: /dev/ttyUSB0): ")
        try:
            self.ser = serial.Serial(self.portName, self.baudrate)
        except serial.serialutil.SerialException:
            print("Can't open : ", self.portName)
            self.dummyPlug = True
            print("Dummy mode activated")

    def close(self):
        if(self.ser.isOpen()):
            self.ser.close()
        else:
            print(self.portName, " it's already closed")

    def getData(self):
        if(True):
            print("hey, I'm reading data from the serial port")
            self.ser.read_all()
            print("supposedly I read something - 1")
            value = self.ser.readline()  # read line (single value) from the serial port
            print("supposedly I read something")
            print(value)
            decoded_bytes = str(value[0:len(value) - 2].decode("utf-8"))
            print(decoded_bytes)
            value_chain = decoded_bytes.split(",")
            print(value_chain)
        else:
            print("dummy mode activated")
            value_chain = [0] + random.sample(range(0, 300), 1) + \
                [random.getrandbits(1)] + random.sample(range(0, 20), 15)
        return value_chain
    
    def sendData(self, command):
        if self.dummyPlug:
            print(f"Dummy mode: Sending command {command}")
        else:
            try:
                self.ser.write(command.encode())  # Send command as bytes
                print(f"Sent command: {command}")
            except serial.serialutil.SerialException as e:
                print(f"Failed to send command: {e}")


    def isOpen(self):
        return self.ser.isOpen()

    def dummyMode(self):
        return self.dummyPlug