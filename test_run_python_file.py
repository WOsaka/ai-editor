import unittest
from functions.run_python_file import run_python_file


class TestRunPythonFile(unittest.TestCase):
    def test_run_python_file(self):
        test_cases = [
            {
                "name": "1",
                "working_directory": "calculator",
                "file_path": "main.py",
            },
            {
                "name": "2",
                "working_directory": "calculator",
                "file_path": "main.py",
                "args": ["3 + 5"],
            },
            {
                "name": "3",
                "working_directory": "calculator",
                "file_path": "tests.py",
            },
            {
                "name": "4",
                "working_directory": "calculator",
                "file_path": "../main.py",
            },
            {
                "name": "5",
                "working_directory": "calculator",
                "file_path": "nonexistent.py",
                "args": [],
            },
            {
                "name": "6",
                "working_directory": "calculator",
                "file_path": "lorem.txt",
            },
        ]

        for test_case in test_cases:
            with self.subTest(test_case=test_case["name"]):
                result = run_python_file(
                    test_case["working_directory"],
                    test_case["file_path"],
                    test_case["args"] if "args" in test_case else None,
                )
                print(f"\nTest Case {test_case['name']}:\n{result}")


if __name__ == "__main__":
    unittest.main(verbosity=2, buffer=False)
