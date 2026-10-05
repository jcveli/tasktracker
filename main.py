import sys
import json

FILE_PATH = 'data.json'


def add_task(task_string):
   data = load_data()


def update_task(task_id, updated_task_string):
    print(f'Updating task {task_id}: {updated_task_string}')


def delete_task(task_id):
    print(f'Deleting task {task_id}')


def mark_task_in_progress(task_id):
    print(f'Marking task {task_id} as in progress')


def mark_task_done(task_id):
    print(f'Marking task {task_id} as done')


def list_tasks(sub_cmd=None):
    print(f'Listing tasks for sub-command')



def load_data():
    try:
        with open(FILE_PATH, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print('File not found, creating new file...')
        with open(file=FILE_PATH, mode='w') as file:
            json.dump(data, file, indent=4)
    except json.JSONDecodeError:
        print('Error decoding JSON data')
        return []

def save_data(data):
    try:
        with open(FILE_PATH, 'w') as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f'Error saving data: {e}')



def main(name):
    print(f'Hi, {name}')  # Press F9 to toggle the breakpoint.
    task = sys.argv[1] if len(sys.argv) > 1 else None

    if task is None:
        print('No task provided')
        return

    #print(f'Task: {task}')


    match task:
        case 'add':
            new_task_string = sys.argv[2] if len(sys.argv) > 2 else None
            if new_task_string is None:
                print('No task string provided')
                return
            add_task(new_task_string)
        case 'update':
            task_id = sys.argv[2] if len(sys.argv) > 2 else None
            if task_id is None:
                print('No task ID provided')
                return
            updated_task_string = sys.argv[3] if len(sys.argv) > 3 else None
            if updated_task_string is None:
                print('No updated task string provided')
                return

            update_task(task_id, updated_task_string)
        case 'delete':
            task_id = sys.argv[2] if len(sys.argv) > 2 else None
            if task_id is None:
                print('No task ID provided')
                return
            delete_task(task_id)
        case 'mark-in-progress':
            task_id = sys.argv[2] if len(sys.argv) > 2 else None
            if task_id is None:
                print('No task ID provided')
                return
            mark_task_in_progress(task_id)
        case 'mark-done':
            task_id = sys.argv[2] if len(sys.argv) > 2 else None
            if task_id is None:
                print('No task ID provided')
                return
            mark_task_done(task_id)
        case 'list':
            sub_cmd = sys.argv[2] if len(sys.argv) > 2 else None

            list_tasks(sub_cmd)
        case _:
            print('Unknown task')



if __name__ == '__main__':
    main('Jerald')

