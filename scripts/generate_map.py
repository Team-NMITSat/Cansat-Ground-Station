import folium
import os
import time
import csv
from selenium import webdriver
import math

from PIL import Image, ImageDraw, ImageFont

from PIL import Image, ImageDraw, ImageFont

def haversine(coord1, coord2):
    """
    Calculate the great circle distance in kilometers between two points 
    on the earth (specified in decimal degrees)
    """
    # Convert decimal degrees to radians
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a))
    r = 6371  # Radius of Earth in kilometers
    return c * r

def create_map_and_save_image(output_dir='generated_graphs', output_file='map_image.png'):
    """
    Generates a map with a path based on coordinates read from a CSV file and saves it as a PNG image.
    
    Args:
    csv_path (str): Path to the CSV file containing coordinates.
    output_dir (str): Directory where the PNG image will be saved.
    output_file (str): Name of the output PNG file.
    """
    # Read coordinates from CSV
    csv_path = 'flight_data.csv'
    coordinates = []
    with open(csv_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            try:
                # Extract latitude and longitude from the 9th and 10th columns
                lat = float(row[9])
                lon = float(row[10])
                coordinates.append((lat, lon))
            except ValueError:
                continue  # Skip rows where conversion fails

    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Create a map centered around the first coordinate
    map_obj = folium.Map(location=coordinates[0], zoom_start=13)
    
    # Add a line to the map with the coordinates
    folium.PolyLine(coordinates, color='red', weight=1).add_to(map_obj)
    # add a line b/w the first and last point
    folium.PolyLine([coordinates[0], coordinates[-1]], color='blue', weight=1).add_to(map_obj)
    
    # Temporary path for the HTML file
    temp_html = os.path.join(output_dir, 'temp_map.html')
    map_obj.save(temp_html)
    
    # Configure WebDriver
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run in headless mode
    options.add_argument('--disable-gpu')  # Disable GPU hardware acceleration
    options.add_argument('--window-size=1920x1080')  # Specify browser resolution
    
    # Set the path to your WebDriver executable
    driver = webdriver.Chrome(options=options)

    # Load the HTML file
    driver.get('file:///' + os.path.abspath(temp_html))

    # Give some time for the page to load
    time.sleep(2)

    # Save the rendered page as a PNG image
    output_path = os.path.join(output_dir, output_file)
    driver.save_screenshot(output_path)

    total_distance = sum(haversine(coordinates[i], coordinates[i + 1]) for i in range(len(coordinates) - 1)) 
    direct_displacement = haversine(coordinates[0], coordinates[-1]) if len(coordinates) > 1 else 0
    
    # Print or return distances as needed
    print(f"Total travel distance: {total_distance:.2f} km")
    print(f"Direct displacement: {direct_displacement:.2f} km")

    # Close the browser and clean up
    driver.quit()
    os.remove(temp_html)  # Remove temporary HTML file
    
    print(f"Map image saved as {output_path}")
