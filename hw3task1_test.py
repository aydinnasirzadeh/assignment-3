import unittest
from unittest.mock import patch
from io import StringIO
import Task_1

class TestMainFunction(unittest.TestCase):
    
    def test_main_output(self):
        expected_output = """Celsius\t\tFahrenheit
0\t\t32
10		50
20		68
30		86
40		104
50		122
60		140
70		158
80		176
90		194
100		212"""
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            Task_1.main()
            self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

if __name__ == "__main__":
    unittest.main()
