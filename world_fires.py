import csv
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline
from datetime import datetime

filename = '/Users/raulgiron/Desktop/Data_Visualization/world_fires_1_day.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # for index, column_header in enumerate(header_row):
    #     print(f"{index}-) {column_header} ", end=' \t')

    # Automatic indexes.
    latitude_index = header_row.index('latitude')
    longitude_index = header_row.index('longitude')
    brightness_index = header_row.index('brightness')
    date_index = header_row.index('acq_date')
    # print(f'\n{latitude_index}, {longitude_index}, {brightness_index}, {date_index}')

    # Get latitude and longitude and brightness from this file.
    latitudes, longitudes, f_brightness = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
        try:
            lat = row[latitude_index]
            lon = row[longitude_index]
            bright = row[brightness_index]
        except ValueError:
            print(f"Check the file for a Value Error.")
        else:
            latitudes.append(lat)
            longitudes.append(lon)
            f_brightness.append(bright)
            # print(lat, lon, bright, current_date, sep=',\t')

    # Map the earthquakes.
    data = [{
        'type': 'scattergeo',
        'lon': longitudes,
        'lat': latitudes,
        # 'text': hover_texts,
        'marker': {
            # 'size': [5 * fire for fire in f_brightness],
            'color': 'red',
            'colorscale': 'Viridis',
            'reversescale': True,
            'colorbar': {'title': 'Magnitude'},
        },
    }]
    my_layout = Layout(title="PROVISIONAL TITLE")

    fig = {'data': data, 'layout': my_layout}
    offline.plot(fig, filename='global_earthquakes.html')
