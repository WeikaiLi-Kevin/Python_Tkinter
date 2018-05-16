"""
Description: unittest test cases
test the situation of reading the CSV file and getting the values in the all columns


---------------------
@author: Weikai Li
Last modify date: 31 Jan, 2018
"""

import unittest
import readCSVFile


class Test(unittest.TestCase):

    def setUp(self):
        """
        read the CSV file
        :return: the pandas frame of the data in the CSV file
        """
        reader = readCSVFile.ReadFile()
        return reader

    def test_IfCSVExist(self):
        """
        test the path of the CSV file exists or not
        """
        reader = self.setUp()
        result = reader.check_file_exist()
        # author is Weikai Li
        print("author is Weikai Li")
        self.assertEqual(result, True)

    def test_Ref_dateNotNone(self):
        """
        test the code get the value in the ref_data column or not
        """
        reader = self.setUp()
        result = reader.get_ref_date()
        self.assertIsNotNone(result[0])

    def test_GeoNotNone(self):
        """
        test the code get the value in the geo column or not
        """
        reader = self.setUp()
        result = reader.get_geo()
        self.assertIsNotNone(result[0])

    def test_CommodNotNone(self):
        """
        test the code get the value in the commod column or not
        """
        reader = self.setUp()
        result = reader.get_commond()
        self.assertIsNotNone(result[0])

    def test_VectorNotNone(self):
        """
        test the code get the value in the vector column or not
        """
        reader = self.setUp()
        result = reader.get_vector()
        self.assertIsNotNone(result[0])

    def test_CoordinateNotNone(self):
        """
        test the code get the value in the coordinate column or not
        """
        reader = self.setUp()
        result = reader.get_coordinate()
        self.assertIsNotNone(result[0])

    def test_ValueNotNone(self):
        """
        test the code get the value in the value column or not
        """
        reader = self.setUp()
        result = reader.get_value()
        self.assertIsNotNone(result[0])


# main function
if __name__ == '__main__':
    unittest.main()
