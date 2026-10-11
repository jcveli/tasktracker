import os
import unittest
from unittest.mock import patch
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

if __name__ == '__main__':
    unittest.main()
