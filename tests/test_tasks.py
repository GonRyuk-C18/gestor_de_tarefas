import unittest
from controllers import create_task, get_all_tasks, change_task, delete_task, tasks

class TestTaskOperations(unittest.TestCase):

    def setUp(self):
        tasks.clear()

    def test_create_task(self):
        t = create_task("Task1", "Descrição da tarefa", "2025-06-01", "3")
        self.assertEqual(len(tasks),1)
        self.assertEqual(t.title, "Task1")
        self.assertEqual(t.status, "Pendente")

        all_tasks = get_all_tasks()
        self.assertEqual(len(all_tasks), 1)
        self.assertEqual(all_tasks[0].title, "Task1")

    def test_change_task(self):
        t = create_task("Task1", "Descrição da tarefa", "2025-06-01", "3")

        changed_task = change_task(0, new_title="Task1.1", new_status="Concluida")
        self.assertIsNotNone(changed_task)
        self.assertEqual(changed_task.title, "Task1.1")
        self.assertEqual(changed_task.status, "Concluida")

    def test_delete_task(self):
        t = create_task("Task1", "Descrição da tarefa", "2025-06-01", "3")

        self.assertEqual(len(tasks), 1)
        result = delete_task(0)
        self.assertTrue(result)
        self.assertEqual(len(tasks), 0)

    def test_delete_task_invalid(self):
        result = delete_task(1)
        self.assertFalse(result)

    if __name__=="__main__":
        unittest.main()