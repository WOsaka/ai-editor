import unittest
from functions.write_file import write_file
from functions.get_files_info import get_files_info
from functions.get_files_content import get_file_content
from functions.run_python_file import run_python_file
import os


# class TestGetFileInfo(unittest.TestCase):
#     def test_get_file_info(self):
#         test_cases = [
#             {
#                 "name": "1",
#                 "working_directory": "calculator",
#                 "directory": ".",
#             },
#             {
#                 "name": "2",
#                 "working_directory": "calculator",
#                 "directory": "pkg",
#             },
#             {
#                 "name": "3",
#                 "working_directory": "calculator",
#                 "directory": "/bin",
#             },
#             {
#                 "name": "4",
#                 "working_directory": "calculator",
#                 "directory": "../",
#             },
#         ]

#         for test_case in test_cases:
#             with self.subTest(test_case=test_case["name"]):
#                 result = get_files_info(
#                     test_case["working_directory"],
#                     test_case["directory"],
#                 )
#                 print(f"\n{test_case['name']}:\n{result}")


# class TestGetFileContent(unittest.TestCase):
#     def test_get_file_content(self):
#         test_cases = [
#             {
#                 "name": "1",
#                 "working_directory": "calculator",
#                 "file_path": "main.py",
#             },
#             {
#                 "name": "2",
#                 "working_directory": "calculator",
#                 "file_path": "pkg/calculator.py",
#             },
#             {
#                 "name": "3",
#                 "working_directory": "calculator",
#                 "file_path": "/bin/cat",
#             },
#             {
#                 "name": "4",
#                 "working_directory": "calculator",
#                 "file_path": "pkg/does_not_exist.py",
#             },
#         ]

#         for test_case in test_cases:
#             with self.subTest(test_case=test_case["name"]):
#                 result = get_file_content(
#                     test_case["working_directory"],
#                     test_case["file_path"],
#                 )
#                 print(f"\n{test_case['name']}:\n{result}")


# class TestWriteFile(unittest.TestCase):
#     def test_write_file(self):
#         test_cases = [
#             {
#                 "name": "1",
#                 "working_directory": "calculator",
#                 "file_path": "lorem.txt",
#                 "content": "wait, this isn't lorem ipsum",
#             },
#             {
#                 "name": "2",
#                 "working_directory": "calculator",
#                 "file_path": "pkg/morelorem.txt",
#                 "content": "lorem ipsum dolor sit amet",
#             },
#             {
#                 "name": "3",
#                 "working_directory": "calculator",
#                 "file_path": "/tmp/temp.txt",
#                 "content": "this should not be allowed",
#             },
#         ]

#         for test_case in test_cases:
#             with self.subTest(test_case=test_case["name"]):
#                 result = write_file(
#                     test_case["working_directory"],
#                     test_case["file_path"],
#                     test_case["content"],
#                 )
#                 print(f"\n{test_case['name']}:\n{result}")

class TestRunPythonFile(unittest.TestCase):
    def test_run_python_file(self):
        test_cases = [
            {
                "name": "1",
                "working_directory": "calculator",
                "file_path": "main.py",
                "args": []
            },
            {
                "name": "2",
                "working_directory": "calculator",
                "file_path": "main.py",
                "args": ["3 + 5"]
            },
            {
                "name": "3",
                "working_directory": "calculator",
                "file_path": "tests.py",
                "args": []
            },
            {
                "name": "4",
                "working_directory": "calculator",
                "file_path": "../main.py",
                "args": []
            },
            {
                "name": "5",
                "working_directory": "calculator",
                "file_path": "nonexistent.py",
                "args": []
            },
        ]

        for test_case in test_cases:
            with self.subTest(test_case=test_case["name"]):
                result = run_python_file(
                    test_case["working_directory"],
                    test_case["file_path"],
                    test_case["args"],
                )
                print(f"\n{test_case['name']}:\n{result}")

if __name__ == "__main__":
    unittest.main(verbosity=2, buffer=False)
