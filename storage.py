import json


FILE_PATH = 'data.json'

def load_tasks():
    try:
        with open(FILE_PATH, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print('File not found, creating new file...')
        with open(file=FILE_PATH, mode='w') as file:
            data = []
            json.dump(data, file, indent=4)
    except json.JSONDecodeError:
        print('Error decoding JSON data')
        return []

def save_tasks(tasks):
    try:
        with open(FILE_PATH, 'w') as file:
            json.dump(tasks, file, indent=4)
    except Exception as e:
        print(f'Error saving tasks: {e}')

