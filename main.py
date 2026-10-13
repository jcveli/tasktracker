import shlex

from task_operations import add_task, update_task, delete_task, mark_task_in_progress, mark_task_done ,list_tasks

#FILE_PATH = 'data.json'

EXIT_COMMANDS = ('q', 'quit')


def run_command(args):
    task = args[0]

    task_id = args[1] if len(args) > 1 else None


    match task:
        case 'add':
            new_task_string = args[1] if len(args) > 1 else None
            if new_task_string is None:
                print('No description of task was provided.')
                return
            add_task(new_task_string)

        case 'update':
            updated_task_string = args[2] if len(args) > 2 else None
            if task_id is None:
                print('No task ID provided')
                return
            try:
                task_id = int(task_id)
            except ValueError:
                print('Task ID must be an integer')
                return

            if updated_task_string is None:
                print('No updated description of task was provided.')
                return


            update_task(task_id, updated_task_string)
        case 'delete':
            if task_id is None:
                print('No task ID provided')
                return

            try:
                task_id = int(task_id)
            except ValueError:
                print('Task ID must be an integer')
                return
            delete_task(task_id)

        case 'mark-in-progress':
            if task_id is None:
                print('No task ID provided')
                return
            try:
                task_id = int(task_id)
            except ValueError:
                print('Task ID must be an integer')
                return

            mark_task_in_progress(task_id)

        case 'mark-done':
            if task_id is None:
                print('No task ID provided')
                return
            try:
                task_id = int(task_id)
            except ValueError:
                print('Task ID must be an integer')
                return
            mark_task_done(task_id)
        case 'list':
            sub_cmd = task_id
            list_tasks(sub_cmd)
        case _:
            print('Unknown task. Available tasks: add, update, delete, mark-in-progress, mark-done, list, Q/Quit to exit')


def main():
    print('Task Tracker. Available tasks: add, update, delete, mark-in-progress, mark-done, list. Type Q or Quit to exit.')

    while True:
        try:
            line = input('> ').strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break

        if not line:
            continue

        if line.lower() in EXIT_COMMANDS:
            break

        try:
            args = shlex.split(line)
        except ValueError as e:
            print(f'Could not parse input: {e}')
            continue

        run_command(args)

    print('Goodbye!')



if __name__ == '__main__':
    main()
