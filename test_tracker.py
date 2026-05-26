import unittest
import os
import main

class TestBookTracker(unittest.TestCase):
    def test_save_and_load(self):
        test_file = "test_temp.json"
        main.DATA_FILE = test_file
        data = [{"author": "Test", "title": "Test", "rating": 4, "date": "2024-01-01"}]
        main.save_books(data)
        self.assertEqual(main.load_books(), data)
        if os.path.exists(test_file): os.remove(test_file)

if __name__ == "__main__":
    unittest.main()