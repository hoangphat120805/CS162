import json
import csv


def read_file(PATH):
    with open(PATH, 'r', encoding='utf-8') as f:
        raw_data = f.read()
    raw_data = raw_data.split('\n')
    return [json.loads(data) for data in raw_data if data != '']

def outputAsJson(PATH, data):
    PATH = PATH + '.json'
    with open(PATH, 'w', encoding='utf-8') as f:
        if len(data) == 0:
            return
        for item in data:
            f.write(json.dumps(item.__dict__, ensure_ascii=False) + '\n')

def outputAsCSV(PATH, data):
    PATH = PATH + '.csv'
    with open(PATH, 'w', newline='', encoding='utf-8') as f:
        if len(data) == 0:
            return
        writer = csv.DictWriter(f, fieldnames=data[0].__dict__.keys())
        writer.writeheader()
        for item in data:
            writer.writerow(item.__dict__)





