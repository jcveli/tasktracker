import sys

from task_operations import add_task, update_task, delete_task, mark_task_in_progress, mark_task_done ,list_tasks

#FILE_PATH = 'data.json'



def main():
    task = sys.argv[1] if len(sys.argv) > 1 else None

    if task is None:
        print('No task provided. Available tasks: add, update, delete, mark-in-progress, mark-done, list')
        return


    task_id = sys.argv[2] if len(sys.argv) > 2 else None


    match task:
        case 'add':
            new_task_string = sys.argv[2] if len(sys.argv) > 2 else None
            if new_task_string is None:
                print('No description of task was provided.')
                return
            add_task(new_task_string)

        case 'update':
            updated_task_string = sys.argv[3] if len(sys.argv) > 3 else None
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
            sub_cmd = sys.argv[2] if len(sys.argv) > 2 else None
            list_tasks(sub_cmd)
        case _:
            print('Unknown task. Available tasks: add, update, delete, mark-in-progress, mark-done, list')



if __name__ == '__main__':
    main()

