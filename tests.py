import unittest
from functions.get_files_info import get_files_info
import os


class TestGetFilesInfo(unittest.TestCase):
    def test_1(self):
        result = get_files_info("calculator", ".")
        print(f"Result for current directory:\n{result}")

    def test_2(self):
        result = get_files_info("calculator", "pkg")
        print(f"Result for 'pkg' directory:\n{result}")

    def test_3(self):
        result = get_files_info("calculator", "/bin")
        print(f"Result for '/bin' directory:\n{result}")

    def test_4(self):
        result = get_files_info("calculator", "../")
        print(f"Result for '../' directory:\n{result}")


if __name__ == "__main__":
    # Run tests with high verbosity to see output
    unittest.main()
