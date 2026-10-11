import os
import unittest
from unittest.mock import patch, Mock
import tempfile



import storage
import task_operations




class TestAddTask(unittest.TestCase):
    def setUp(self):
        # Runs before each test. Points storage at a temporary file
        # so the tests never touch your real data.json.
        self.temp_dir = tempfile.TemporaryDirectory()
        self.patcher = patch.object(
            storage, 'FILE_PATH', os.path.join(self.temp_dir.name, 'test.json')
        )
        self.patcher.start()


    def tearDown(self):
        # Runs after each test. Cleans up the temporary file.
        self.patcher.stop()
        self.temp_dir.cleanup()


    def test_add_creates_task_with_not_started_status(self):
        task_operations.add_task('buy eggs')

        tasks = storage.load_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]['description'], 'buy eggs')
        self.assertEqual(tasks[0]['status'], 'not-started')


    def test_second_task_gets_id_2(self):
        task_operations.add_task('buy eggs')
        task_operations.add_task('buy milk')

        tasks = storage.load_tasks()
        self.assertEqual(tasks[1]['id'], 2)




class TestUpdateTask(unittest.TestCase):
    def setUp(self):
        # Runs before each test. Points storage at a temporary file
        # so the tests never touch your real data.json.
        self.temp_dir = tempfile.TemporaryDirectory()
        self.patcher = patch.object(
            storage, 'FILE_PATH', os.path.join(self.temp_dir.name, 'test.json')
        )
        self.patcher.start()

    def tearDown(self):
        # Runs after each test. Cleans up the temporary file.
        self.patcher.stop()
        self.temp_dir.cleanup()

    def test_update_task_on_unknown_id(self):
        task_operations.add_task('buy eggs')
        tasks_before_update = storage.load_tasks()
        with patch('builtins.print') as mock_print:
            task_operations.update_task(999, 'buy milk')
            mock_print.assert_called_with('Task with ID 999 not found')
        tasks_after_update = storage.load_tasks()
        self.assertEqual(tasks_after_update, tasks_before_update)

    def test_update_changes_description_and_updated_at(self):
        with patch('task_operations.get_current_timestamp', return_value='2026-01-01 09:00:00'):
            task_operations.add_task('buy eggs')

        original = storage.load_tasks()[0]

        with patch('task_operations.get_current_timestamp', return_value='2026-01-02 09:00:00'):
            task_operations.update_task(1, 'buy organic eggs')

        updated = storage.load_tasks()[0]
        self.assertEqual(updated['description'], 'buy organic eggs')
        self.assertEqual(updated['created_at'], original['created_at'])
        self.assertEqual(updated['updated_at'], '2026-01-02 09:00:00')



class TestSaveTasks(unittest.TestCase):
    def setUp(self):
        # Runs before each test. Points storage at a temporary file
        # so the tests never touch your real data.json.
        self.temp_dir = tempfile.TemporaryDirectory()
        self.patcher = patch.object(
            storage, 'FILE_PATH', os.path.join(self.temp_dir.name, 'test.json')
        )
        self.patcher.start()

    def tearDown(self):
        self.patcher.stop()
        self.temp_dir.cleanup()


    def test_failed_save_keeps_original_data(self):
        task_operations.add_task('buy eggs')
        original_data = storage.load_tasks()

        # Patch json.dump to raise an exception when called
        with patch('json.dump', side_effect=Exception('Simulated save error')):
            with patch('builtins.print') as mock_print:
                task_operations.add_task('buy milk')
                mock_print.assert_called_with('Error saving tasks: Simulated save error')

        # Ensure the original data is still intact
        current_data = storage.load_tasks()
        self.assertEqual(current_data, original_data)


class TestDeleteTask(unittest.TestCase):
    def setUp(self):
        # Runs before each test. Points storage at a temporary file
        # so the tests never touch your real data.json.
        self.temp_dir = tempfile.TemporaryDirectory()
        self.patcher = patch.object(
            storage, 'FILE_PATH', os.path.join(self.temp_dir.name, 'test.json')
        )
        self.patcher.start()

    def tearDown(self):
        # Runs after each test. Cleans up the temporary file.
        self.patcher.stop()
        self.temp_dir.cleanup()

    def test_delete_task_on_unknown_id(self):
        task_operations.add_task('buy eggs')
        tasks_before_delete = storage.load_tasks()

        with patch('builtins.print') as mock_print:
            task_operations.delete_task(999)
            mock_print.assert_called_with('Task with ID 999 not found')

        tasks_after_delete = storage.load_tasks()
        self.assertEqual(tasks_after_delete, tasks_before_delete)

    def test_delete_existing_task_removes_it(self):
        task_operations.add_task('buy eggs')

        with patch('builtins.print') as mock_print:
            task_operations.delete_task(1)
            mock_print.assert_called_once_with('Deleted task 1 successfully')

        self.assertEqual(storage.load_tasks(), [])

    def test_delete_only_removes_target_task(self):
        task_operations.add_task('buy eggs')
        task_operations.add_task('buy milk')

        with patch('builtins.print'):
            task_operations.delete_task(1)

        remaining = storage.load_tasks()
        self.assertEqual(len(remaining), 1)
        self.assertEqual(remaining[0]['id'], 2)
        self.assertEqual(remaining[0]['description'], 'buy milk')



class TestMarkTaskInProgress(unittest.TestCase):
    def setUp(self):
        # Runs before each test. Points storage at a temporary file
        # so the tests never touch your real data.json.
        self.temp_dir = tempfile.TemporaryDirectory()
        self.patcher = patch.object(
            storage, 'FILE_PATH', os.path.join(self.temp_dir.name, 'test.json')
        )
        self.patcher.start()

    def tearDown(self):
        # Runs after each test. Cleans up the temporary file.
        self.patcher.stop()
        self.temp_dir.cleanup()

    def test_mark_task_in_progress_on_unknown_id(self):
        task_operations.add_task('buy eggs')
        tasks_before_mark = storage.load_tasks()

        with patch('builtins.print') as mock_print:
            task_operations.mark_task_in_progress(999)
            mock_print.assert_called_with('Task with ID 999 not found')

        tasks_after_mark = storage.load_tasks()
        self.assertEqual(tasks_after_mark, tasks_before_mark)

    def test_mark_task_in_progress_changes_status_and_updated_at(self):
        with patch('task_operations.get_current_timestamp', return_value='2026-01-01 09:00:00'):
            task_operations.add_task('buy eggs')

        original = storage.load_tasks()[0]

        with patch('task_operations.get_current_timestamp', return_value='2026-01-02 09:00:00'):
            task_operations.mark_task_in_progress(1)

        updated = storage.load_tasks()[0]
        self.assertEqual(updated['status'], 'in-progress')
        self.assertEqual(updated['created_at'], original['created_at'])
        self.assertEqual(updated['updated_at'], '2026-01-02 09:00:00')

if __name__ == '__main__':
    unittest.main()
