import json

filename = 'data/eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)
readable_file = 'data/readable_eq_data.json'
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent = 4)

all_eq_data = all_eq_data.get('features','')

mags = [eq_dict['properties']['mag'] for eq_dict in all_eq_data]

print(mags[:10])