import requests
import csv

def main():
    r = requests.get('https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.csv')
    with open('data.csv', 'w') as data_csv:
        data_csv.write(r.text)

    with open('data.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        csv_file.seek(0)
        header = next(csv_file)
        csv_file.seek(0)
        data = []
        for line in csv_reader:
            data.append(dict(line))
        
        print(len(data))
        print(header)


if __name__ == '__main__':
    main()