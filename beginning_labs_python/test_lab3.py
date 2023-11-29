import unittest
from lab3 import chesar


class MyTestCase(unittest.TestCase):
    def test_1(self):
        with open("resources/test_file.txt", "w", encoding='utf-8') as file:
            print("Мама мыла раму!", file=file)
        self.assertEqual(chesar("resources/test_file.txt", 12, "russian"), "Шлшл шжчл ьлшя!\n")

    def test_2(self):
        with open("resources/test_file.txt", "w", encoding='utf-8') as file:
            print("Мама мыла раму!", file=file)
        self.assertEqual(chesar("resources/test_file.txt", 34, "russian"), None)

    def test_3(self):
        with open("resources/test_file.txt", "w", encoding='utf-8') as file:
            print("Мама мыла раму!", file=file)
        self.assertEqual(chesar("resources/test_file.txt", 0, "russian"), "Мама мыла раму!\n")

    def test_4(self):
        with open("resources/test_file.txt", "w", encoding='utf-8') as file:
            print("Do you want to play football?", file=file)
        self.assertEqual(chesar("resources/test_file.txt", 5, "english"), "It dtz bfsy yt uqfd kttygfqq?\n")

    def test_5(self):
        with open("resources/test_file.txt", "w", encoding='utf-8') as file:
            print("Do you want to play football?", file=file)
        self.assertEqual(chesar("resources/test_file.txt", 27, "english"), None)

    def test_6(self):
        with open("resources/test_file.txt", "w", encoding='utf-8') as file:
            print("Do you want to play football?", file=file)
        self.assertEqual(chesar("resources/test_file.txt", 0, "english"), "Do you want to play football?\n")


if __name__ == '__main__':
    unittest.main()
