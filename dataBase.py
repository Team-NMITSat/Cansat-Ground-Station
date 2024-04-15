import time
import csv
from scripts.generate_map import create_map_and_save_image
from scripts.generate_graphs import create_graphs_save_images

class data_base():
    def __init__(self):
        self.state = False

    def guardar(self, data):
        if self.state == True:
            data.append(time.asctime())
            with open("flight_data.csv", "a") as f:
                writer = csv.writer(f, delimiter=",")
                writer.writerow(data)

    def start(self):
        self.state = True
        print('starting storage in csv')

    def stop(self):
        self.state = False
        create_map_and_save_image()
        create_graphs_save_images()
        print('stopping storage in csv')
