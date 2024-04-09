import unittest
from io import StringIO
from unittest.mock import patch
import Task_2

class TestMainFunction(unittest.TestCase):

    @patch('builtins.input', side_effect=["5", "1", "2", "3", "4", "5"])
    def test_main_input_calls(self, mock_input):
        Task_2.main() 
        expected_calls = ["Max number to compute the average value: "]
        expected_calls.extend([f"Value {i+1}: " for i in range(5)])
        # Check if input was called with the expected arguments
        self.assertEqual(mock_input.call_args_list, [unittest.mock.call(arg) for arg in expected_calls])

    def test_average(self):
        test_cases = [
            {'input': [12, 57, 67, -17, 89, 83, 87, 61, -21, 96, 99, 49, 98], 'expected_output': 'Average value: 62.33'},
            {'input': [4, 21, 27, 60, 25], 'expected_output': 'Average value: 33.25'},
            {'input': [1, 17], 'expected_output': 'Average value: 17.00'},
            {'input': [25, -33, 54, 96, -26, -36, 79, 27, -1, -36, 63, 39, 0, 74, 63, 62, 90, 60, -30, 69, 18, 2, -15, -39, -40, -9], 'expected_output': 'Average value: 21.24'},
        ]
        for test_case in test_cases:
            with patch('builtins.input', side_effect=test_case['input']), \
                 patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                Task_2.main()
            self.assertEqual(mock_stdout.getvalue().strip(), test_case['expected_output'])

    def test_invalid_input(self):
        test_cases = [
            {'input': [-5], 'expected_output': 'Error message'},
            {'input': [0], 'expected_output': 'Error message'},
        ]
        for test_case in test_cases:
            with patch('builtins.input', side_effect=test_case['input']), \
                 patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                Task_2.main()
            self.assertEqual(mock_stdout.getvalue().strip(), test_case['expected_output'])

if __name__ == '__main__':
    unittest.main()
