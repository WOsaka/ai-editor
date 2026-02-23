import unittest
from functions.write_file import write_file


class TestWriteFile(unittest.TestCase):
    def test_write_file(self):
        test_cases = [
            {
                "name": "1",
                "working_directory": "calculator",
                "file_path": "lorem.txt",
                "content": "wait, this isn't lorem ipsum",
            },
            {
                "name": "2",
                "working_directory": "calculator",
                "file_path": "pkg/morelorem.txt",
                "content": "lorem ipsum dolor sit amet",
            },
            {
                "name": "3",
                "working_directory": "calculator",
                "file_path": "/tmp/temp.txt",
                "content": "this should not be allowed",
            },
            {
                "name": "4",
                "working_directory": "calculator",
                "file_path": "pkg/test/evenmorelorem.txt",
                "content": "lorem ipsum dolor sit amet",
            },
        ]

        for test_case in test_cases:
            with self.subTest(test_case=test_case["name"]):
                result = write_file(
                    test_case["working_directory"],
                    test_case["file_path"],
                    test_case["content"],
                )
                print(f"\nTest Case {test_case['name']}:\n{result}")


if __name__ == "__main__":
    unittest.main(verbosity=2, buffer=False)
