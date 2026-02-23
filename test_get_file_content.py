import unittest
from functions.get_files_content import get_file_content


class TestGetFileContent(unittest.TestCase):
    def test_get_file_content(self):
        test_cases = [
            {
                "name": "1",
                "working_directory": "calculator",
                "file_path": "main.py",
            },
            {
                "name": "2",
                "working_directory": "calculator",
                "file_path": "pkg/calculator.py",
            },
            {
                "name": "3",
                "working_directory": "calculator",
                "file_path": "/bin/cat",
            },
            {
                "name": "4",
                "working_directory": "calculator",
                "file_path": "pkg/does_not_exist.py",
            },
            {
                "name": "5",
                "working_directory": "calculator",
                "file_path": "lorem.txt",
            },
        ]

        for test_case in test_cases:
            with self.subTest(test_case=test_case["name"]):
                result = get_file_content(
                    test_case["working_directory"],
                    test_case["file_path"],
                )
                print(f"\nTest Case {test_case['name']}:\n{result}")


if __name__ == "__main__":
    unittest.main(verbosity=2, buffer=False)
