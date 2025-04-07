import unittest
import os
from timer import example, execution_timer

class TestExecutionTimer(unittest.TestCase):

    def test_example_function_output(self):
        """Перевірка, що функція повертає правильне значення"""
        result = example(0.1)
        self.assertEqual(result, "done")

    def test_log_file_created(self):
        """Перевірка, що файл логів створений"""
        self.assertTrue(os.path.exists('execution.log'))

    def test_log_contains_function_name(self):
        """Перевірка, що ім'я функції є в логах"""
        with open('execution.log', 'r') as f:
            logs = f.read()
        self.assertIn("Function 'example' executed", logs)

    def test_timer_on_custom_function(self):
        """Перевірка, що декоратор працює з іншими функціями"""
        @execution_timer
        def add(x, y):
            return x + y
        self.assertEqual(add(3, 7), 10)

if __name__ == '__main__':
    unittest.main()
