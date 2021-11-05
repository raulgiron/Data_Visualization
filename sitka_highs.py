import csv
import matplotlib.pyplot as plt
from datetime import datetime


filename = "/Users/raulgiron/Desktop/Data_Visualization/data/sitka_weather_2018_simple.csv"
with open(filename) as file_object:
    reader = csv.reader(file_object)
    header_row = next(reader)
    # for index, column_header in enumerate(header_row, 1):
    #     print(f"{index}-) {column_header}", end=' \t')

    # Get dates and high temperatures from this file.
    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = (int(row[5]) - 32) * 5/9
        dates.append(current_date)
        highs.append(high)
    # print(highs)

# Plot the high temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')

# Format plot.
ax.set_title("Daily high temperatures - 2018", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Temperature (C)', fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()
