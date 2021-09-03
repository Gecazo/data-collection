import csv 
import matplotlib.pyplot as plt

filename = 'data/sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    highs = [int(row[5]) for row in reader]
    
    print(highs)

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(highs, c='red')

ax.set_title("Highest temperature of the day", fontsize=24)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()