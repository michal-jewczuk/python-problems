import unittest

import example as example

class TestSortedWithoutMinMax(unittest.TestCase):

    def test_with_empty_list(self):
        initial = []
        expected = []

        result = example.getSortedWithoutMinMax(initial)

        self.assertEqual(result, expected)

    def test_with_one_element(self):
        initial = [-1]
        expected = []

        result = example.getSortedWithoutMinMax(initial)

        self.assertEqual(result, expected)

    def test_with_two_elements(self):
        initial = [89,-1]
        expected = []

        result = example.getSortedWithoutMinMax(initial)

        self.assertEqual(result, expected)

    def test_with_three_elements(self):
        initial = [5,89,-1]
        expected = [5]

        result = example.getSortedWithoutMinMax(initial)

        self.assertEqual(result, expected)

    def test_with_multiple_elements(self):
        testData = [
                ([3,3,3,3], [3,3]),
                ([5,6,7,8], [6,7]),
                ([9,8,7,6,5], [6,7,8]),
                ([-100,55,12,4,121,-4], [-4,4,12,55]),
                (['ccc', 'aaa', 'ddd', 'eee', 'bbb'], ['bbb', 'ccc', 'ddd'])
                ]

        for data in testData:
            result = example.getSortedWithoutMinMax(data[0])
            self.assertEqual(result, data[1])

    def test_with_no_list(self):
        expected = "You need to supply an array with sortable elements"

        with self.assertRaises(ValueError) as error:
            example.getSortedWithoutMinMax(1)
        self.assertEqual(str(error.exception), expected)

    def test_with_string_as_argument(self):
        expected = "You need to supply an array with sortable elements"

        with self.assertRaises(ValueError) as error:
            example.getSortedWithoutMinMax('test')
        self.assertEqual(str(error.exception), expected)



if __name__ == '__main__':
    unittest.main()

