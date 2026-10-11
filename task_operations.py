from storage import load_tasks, save_tasks
from datetime import datetime



def get_current_timestamp():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def get_next_task_id(tasks):
    if not tasks:
        return 1
    max_id = max(task['id'] for task in tasks)

    return max_id + 1



def add_task(task_string):
    data = load_tasks()
    new_task_id = get_next_task_id(data)
    new_task = {
        'id': new_task_id,
        'description': task_string,
        'status': 'not-started',
        'created_at': get_current_timestamp(),
        'updated_at': get_current_timestamp()
    }
    data.append(new_task)
    save_tasks(data)


def update_task(task_id, updated_task_string):
    data = load_tasks()
    for task in data:
        if task['id'] == task_id:
            task['description'] = updated_task_string
            task['updated_at'] = get_current_timestamp()
            save_tasks(data)
            print(f'Updated task {task_id} successfully')
            return

    print(f'Task with ID {task_id} not found')


def delete_task(task_id):
    data = load_tasks()
    data_task = [task for task in data if task['id'] != task_id]

    if len(data) == len(data_task):
        print(f'Task with ID {task_id} not found')
        return

    save_tasks(data_task)
    print(f'Deleted task {task_id} successfully')

def mark_task_in_progress(task_id):
    data = load_tasks()
    for task in data:
        if task['id'] == task_id:
            task['status'] = 'in-progress'
            task['updated_at'] = get_current_timestamp()
            save_tasks(data)
            print(f'Marked task {task_id} as in progress')
            return

    print(f'Task with ID {task_id} not found')

def mark_task_done(task_id):
    data = load_tasks()
    for task in data:
        if task['id'] == task_id:
            task['status'] = 'done'
            task['updated_at'] = get_current_timestamp()
            save_tasks(data)
            print(f'Marked task {task_id} as done')
            return

    print(f'Task with ID {task_id} not found')

def list_tasks(sub_cmd=None):
    data = load_tasks()

    list_filters = {
        None: ['not-started', 'in-progress', 'done'],
        'not-done': ['not-started', 'in-progress'],
        'not-started': ['not-started'],
        'in-progress': ['in-progress'],
        'done': ['done']
   }

    if sub_cmd not in list_filters:
        print(f'Unknown sub-command: {sub_cmd}. Valid options are: {list(list_filters.keys())}')
        return

    for task in data:
        if task['status'] in list_filters[sub_cmd]:
            print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}, Created At: {task['created_at']}, Updated At: {task['updated_at']}")