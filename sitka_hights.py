import csv 

filename = 'data/sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    highs = [int(row[5]) for row in reader]
    
    print(highs)

