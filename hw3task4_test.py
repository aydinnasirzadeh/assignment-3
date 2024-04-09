import unittest
from unittest.mock import patch
from io import StringIO
import Task_4


class TestMainFunction(unittest.TestCase):

    @patch('builtins.input', side_effect=['14', '3', '38', '22', 'end'])
    def test_main_input_calls(self, mock_input):
        Task_4.main()
        expected_calls = [
            'Enter the age of guest (\'end\' to quit): ',
            'Enter the age of guest (\'end\' to quit): ',
            'Enter the age of guest (\'end\' to quit): ',
            'Enter the age of guest (\'end\' to quit): ',
            'Enter the age of guest (\'end\' to quit): ',
        ]
        self.assertEqual(mock_input.call_args_list, [unittest.mock.call(arg) for arg in expected_calls])

    @patch('builtins.input', side_effect=['end'])
    def test_price_with_empty_input(self,mock_input):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            Task_4.main()
            self.assertEqual("The total for that group is $0.00\n", mock_stdout.getvalue())

    def test_total_price(self):
        test_cases = [
            {'input': [13, 59, 10, 68, 65, 19, 6, 25, 66, 52, 1, 33, 2, 10, 47, 'end'], 'expected_output': 'The total for that group is $257.00'},
            {'input': [37, 25, 8, 17, 70, 'end'], 'expected_output': 'The total for that group is $101.00'},
            {'input': [54, 43, 45, 'end'], 'expected_output': 'The total for that group is $69.00'},
            {'input': [65, 16, 16, 64, 67, 50, 66, 34, 46, 64, 4, 11, 38, 8, 52, 19, 53, 60, 65, 21, 16, 5, 13, 'end'], 'expected_output': 'The total for that group is $473.00'},
        ]
        for test_case in test_cases:
            with patch('builtins.input', side_effect=test_case['input']), \
                 patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                Task_4.main()
            self.assertEqual(mock_stdout.getvalue().strip(), test_case['expected_output'])



if __name__ == '__main__':
    unittest.main()
