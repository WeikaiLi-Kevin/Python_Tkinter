"""
Description: read the CSV file and put the data of all columns into lists

---------------------
@author: Weikai Li
Last modify date: 31 Jan, 2018
"""
import pandas as pd
# import os.path to check the CSV file exists or not
import os.path


class ReadFile:

    # get the csv file and give a name for the file
    csvFile = "03290040-eng.csv"

    # initialize six variables as lists to use for the information in the six columns in the csv file provided
    ref_data = []
    geo = []
    commod = []
    vector = []
    coordinate = []
    value = []

    # constructor
    def __init__(self):
        """
        Constructor
        """
        self.open_file()
    # author is Weikai Li

    def open_file(self):
        """
        open_file function is used to read the CSV file and assign them to the defined variables
        """
        df = pd.read_csv(self.csvFile)
        self.ref_data = df['Ref_Date'].tolist()
        self.geo = df['GEO'].tolist()
        self.commod = df['COMMOD'].tolist()
        self.vector = df['Vector'].tolist()
        self.coordinate = df['Coordinate'].tolist()
        self.value = df['Value'].tolist()
        self.value.sort()

    def get_ref_date(self):
        """
        Getter : get the list of ref_data column in the CSV file
        """
        return self.ref_data

    def get_geo(self):
        """
        Getter : get the list of geo column in the CSV file
        """
        return self.geo

    def get_commond(self):
        """
        Getter : get the list of commod column in the CSV file
        """
        return self.commod

    def get_vector(self):
        """
        Getter : get the list of vector column in the CSV file
        """
        return self.vector

    def get_coordinate(self):
        """
        Getter : get the list of coordinate column in the CSV file
        """
        return self.coordinate

    def get_value(self):
        """
        Getter : get the list of value column in the CSV file
        """
        return self.value

    def check_file_exist(self):
        isFile = os.path.isfile("03290040-eng.csv")
        return isFile
    #   author is Weikai Li