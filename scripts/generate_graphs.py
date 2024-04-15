import matplotlib.pyplot as plt
import csv

BASE_DIR = 'generated_graphs/'
# create a dir to save the plot
import os
if not os.path.exists(BASE_DIR):
    os.makedirs(BASE_DIR)


# Data for plotting
x = [1, 2, 3, 4, 5]  # X-axis data
y = [2, 3, 5, 7, 11] # Y-axis data

# Creating the plot
plt.figure(figsize=(8, 6))  # Size of the figure
plt.plot(x, y, label='Altitude')  # Plotting the line
plt.title('Simple Line Plot')  # Title of the plot
plt.xlabel('X axis')  # Label for the X axis
plt.ylabel('Y axis')  # Label for the Y axis
plt.legend()  # Legend to explain plot elements

plt.text(1.0, 0.0, 'Your Data Here', fontsize=12, color='red',
         horizontalalignment='right', verticalalignment='bottom', transform=plt.gca().transAxes)

# Save the plot as a PNG file
plt.savefig(BASE_DIR + 'line_plot.png')
