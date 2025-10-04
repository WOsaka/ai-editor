import unittest
from functions.get_files_content import get_file_content
import os


class TestGetFileContent(unittest.TestCase):
    def test_get_file_content(self):
        test_cases = [
            {
                "name": "main_py_file",
                "working_directory": "calculator",
                "file_path": "main.py",
                "description": "Content of main.py file",
            },
            {
                "name": "get_files_info_py",
                "working_directory": "calculator",
                "file_path": "pkg/calculator.py",
                "description": "Content of calculator.py file",
            },
            {
                "name": "nonexistent_file",
                "working_directory": "calculator",
                "file_path": "/bin/cat",
                "description": "Error",
            },
            {
                "name": "outside_directory",
                "working_directory": "calculator",
                "file_path": "pkg/does_not_exist.py",
                "description": "Error",
            },
        ]

        for test_case in test_cases:
            with self.subTest(test_case=test_case["name"]):
                result = get_file_content(
                    test_case["working_directory"], test_case["file_path"]
                )
                print(f"\n{test_case['description']}:\n{result}")

                # Add assertions based on expected behavior
                self.assertIsInstance(result, str)
                if "Error:" in test_case["description"]:
                    self.assertTrue(result.startswith("Error:"))
                else:
                    self.assertGreater(len(result), 0)


if __name__ == "__main__":
    # Run tests with high verbosity to see output
    unittest.main(verbosity=2, buffer=False)
