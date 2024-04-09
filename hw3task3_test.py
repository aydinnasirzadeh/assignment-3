import unittest
from unittest.mock import patch
from io import StringIO
import Task_3
from random import choice, randint

class TestMainFunction(unittest.TestCase):
    @patch('builtins.input', side_effect=['A', 'B+', 'C-', 'end'])
    def test_main_input_calls(self, mock_input):
        Task_3.main()
        expected_calls = [
            'Enter the grade(\'end\' to quit): ',
            'Enter the grade(\'end\' to quit): ',
            'Enter the grade(\'end\' to quit): ',
            'Enter the grade(\'end\' to quit): '
        ]
        self.assertEqual(mock_input.call_args_list, [unittest.mock.call(arg) for arg in expected_calls])

    @patch('builtins.input', side_effect=['end'])
    def test_average_with_empty_input(self,mock_input):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            Task_3.main()
            #self.assertNotIn('Average', mock_stdout.getvalue())
            self.assertEqual("\nA grade point average: 0.0\n", mock_stdout.getvalue())
    
    def test_average(self):
        data = {"A+": 4.0, "A":4.0, "A-":3.7, "B+":3.3, "B":3.0, "B-":2.7, "C+":2.3, "C":2.0,  "C-":1.7, "D+":1.3, "D":1.0, "F":0.0}
        example = [choice(list(data.items()))[0] for i in range(randint(5,50))]
        ave = sum(data[grade] for grade in example if grade in data)
        expected_output = f"A grade point average: {ave/(len(example)):.1f}"
        example.append("end")
        with patch('builtins.input', side_effect=example), \
             patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            Task_3.main()    
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

if __name__ == "__main__":
    unittest.main()
