import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.dates as mdates
import csv
import os

BASE_DIR = 'generated_graphs/'
if not os.path.exists(BASE_DIR):
    os.makedirs(BASE_DIR)

def safe_parse_date(date_str, default_date='2000-01-01'):
    try:
        return datetime.strptime(date_str, '%d/%m/%Y')
    except ValueError:
        return datetime.strptime(default_date, '%Y-%m-%d')
    
    
def create_graphs_save_images():
    csv_path = 'flight_data.csv'
    accel, altitude, temp, pressure, gyro, gps, dates, battery, speed = [], [], [], [], [], [], [], [], []

    with open(csv_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            try:
                accel.append((float(row[0]), float(row[1]), float(row[2])))
                altitude.append(float(row[3]))
                temp.append(float(row[4]))
                pressure.append(float(row[5]))
                gyro.append((float(row[6]), float(row[7]), float(row[8])))
                gps.append((float(row[9]), float(row[10])))
                dates.append(safe_parse_date(row[11]))
                battery.append(float(row[12]))
                speed.append(float(row[13]))
            except Exception as e:
                print(e)
                continue

    # Define plot layout
    fig, axs = plt.subplots(3, 3, figsize=(15, 15))  # 3 rows, 3 columns

    # Altitude
    axs[0, 0].plot(range(len(altitude)), altitude, label='Altitude')
    axs[0, 0].set_title('Altitude Plot')
    axs[0, 0].set_ylabel('Altitude (m)')
    axs[0 , 0].set_xticklabels([])  
    axs[0, 0].set_xlabel('Time')
    axs[0, 0].legend()

    # Temperature
    axs[0, 1].plot(range(len(temp)), temp, label='Temperature')
    axs[0, 1].set_title('Temperature Plot')
    axs[0, 1].set_ylabel('Temperature (C)')
    axs[0 , 0].set_xticklabels([])  
    axs[0, 0].set_xlabel('Time')
    axs[0, 1].legend()

    # Pressure
    axs[0, 2].plot(range(len(pressure)), pressure, label='Pressure')
    axs[0, 2].set_title('Pressure Plot')
    axs[0, 2].set_ylabel('Pressure (Pa)')
    axs[0 , 0].set_xticklabels([])  
    axs[0, 0].set_xlabel('Time')
    axs[0, 2].legend()

    # Battery
    axs[1, 0].plot(range(len(battery)), battery, label='Battery')
    axs[1, 0].set_title('Battery Plot')
    axs[1, 0].set_ylabel('Battery (%)')
    axs[0 , 0].set_xticklabels([])  
    axs[0, 0].set_xlabel('Time')
    axs[1, 0].legend()

    # GPS
    axs[1, 1].plot([x for x, _ in gps], [y for _, y in gps], 'o', label='GPS Coordinates')
    axs[1, 1].set_title('GPS Plot')
    axs[1, 1].set_ylabel('Coordinates')
    axs[0 , 0].set_xticklabels([])  
    axs[0, 0].set_xlabel('Time')
    axs[1, 1].legend()

    # Accelerometer
    axs[1, 2].plot(range(len(accel)), [x for x, _, _ in accel], label='Accel X')
    axs[1, 2].plot(range(len(accel)), [y for _, y, _ in accel], label='Accel Y')
    axs[1, 2].plot(range(len(accel)), [z for _, _, z in accel], label='Accel Z')
    axs[1, 2].set_title('Accelerometer Plot')
    axs[1, 2].set_ylabel('Acceleration')
    axs[0 , 0].set_xticklabels([])  
    axs[0, 0].set_xlabel('Time')
    axs[1, 2].legend()

    # Gyroscope
    axs[2, 0].plot(range(len(gyro)), [x for x, _, _ in gyro], label='Gyro X')
    axs[2, 0].plot(range(len(gyro)), [y for _, y, _ in gyro], label='Gyro Y')
    axs[2, 0].plot(range(len(gyro)), [z for _, _, z in gyro], label='Gyro Z')
    axs[2, 0].set_title('Gyroscope Plot')
    axs[2, 0].set_ylabel('Gyroscope')
    axs[0 , 0].set_xticklabels([])  
    axs[0, 0].set_xlabel('Time')
    axs[2, 0].legend()

    # Optionally, hide the unused plots
    axs[2, 1].axis('off')
    axs[2, 2].axis('off')

    # Adjust layout and save the combined plot
    plt.tight_layout()
    plt.savefig(BASE_DIR + 'combined_plots.png')

create_graphs_save_images()
