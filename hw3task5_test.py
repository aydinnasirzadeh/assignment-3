import unittest
from unittest.mock import patch
from io import StringIO
import Task_5

class TestMainFunction(unittest.TestCase):

    @patch('builtins.input', side_effect=['0', '0', '3', '0', '3', '2', 'end'])
    def test_main_input_calls(self, mock_input):
        Task_5.main()
        expected_calls = [
            'Enter the x part of the coordinate: ',
            'Enter the y part of the coordinate: ',
            'Enter the x part of the coordinate (\'end\' to quit): ',
            'Enter the y part of the coordinate: ',
            'Enter the x part of the coordinate (\'end\' to quit): ',
            'Enter the y part of the coordinate: ',
            'Enter the x part of the coordinate (\'end\' to quit): '
        ]
        self.assertEqual(mock_input.call_args_list, [unittest.mock.call(arg) for arg in expected_calls])
  
    @patch('builtins.input', side_effect=['0', '0', '3', '0', '3', '4', '0', '4', 'end'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_perimeter_rectangle(self, mock_stdout, mock_input):
        Task_5.main()
        expected_output = "The perimeter of that polygon is 14.00\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('builtins.input', side_effect=['-3', '0', '0', '4', '6', '-2', 'end'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_perimeter_triangle(self, mock_stdout, mock_input):
        Task_5.main()
        expected_output = "The perimeter of that polygon is 22.70\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('builtins.input', side_effect=['-1', '-1', '1', '1', '3', '1', '6', '-3', '4', '-6', 'end'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_perimeter_negative_coordinates(self, mock_stdout, mock_input):
        Task_5.main()
        expected_output = "The perimeter of that polygon is 20.51\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('builtins.input', side_effect=['0', '0', '0', '0', 'end'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_perimeter_single_point(self, mock_stdout, mock_input):
        Task_5.main()
        expected_output = "The perimeter of that polygon is 0.00\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)


if __name__ == "__main__":
    unittest.main()
