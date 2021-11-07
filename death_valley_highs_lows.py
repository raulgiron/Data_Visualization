import csv
import matplotlib.pyplot as plt
from datetime import datetime


filename = '/Users/raulgiron/Desktop/Data_Visualization/data/death_valley_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # for index, column_header in enumerate(header_row, 1):
    #     print(f"{index}-) {column_header} ", end=' \t')

    # Automatic indexes.
    date_index = header_row.index('DATE')
    high_index = header_row.index('TMAX')
    low_index = header_row.index('TMIN')

    # Get dates and high and low temperatures from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
        try:
            high = (int(row[high_index]) - 32) * 5 / 9
            low = (int(row[low_index]) - 32) * 5 / 9
        except ValueError:
            print(f"missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
            # print(highs)

# Plot the high and low temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot.
title = "Daily high and low temperatures - 2018\nDeath Valley, CA"
ax.set_title(title, fontsize=20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Temperature (C)', fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()
