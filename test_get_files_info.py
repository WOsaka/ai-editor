import unittest
from functions.write_file import write_file
from functions.get_files_info import get_files_info
from functions.run_python_file import run_python_file


class TestGetFileInfo(unittest.TestCase):
    def test_get_file_info(self):
        test_cases = [
            {
                "working_directory": "calculator",
                "directory": ".",
            },
            {
                "working_directory": "calculator",
                "directory": "pkg",
            },
            {
                "working_directory": "calculator",
                "directory": "/bin",
            },
            {
                "working_directory": "calculator",
                "directory": "../",
            },
        ]

        for test_case in test_cases:
            with self.subTest(test_case=test_case["directory"]):
                result = get_files_info(
                    test_case["working_directory"],
                    test_case["directory"],
                )
                print(f"\nResult for '{test_case['directory']}' directory:\n{result}")


if __name__ == "__main__":
    unittest.main(verbosity=2, buffer=False)
