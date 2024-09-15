import unittest
from io import StringIO
from datetime import datetime
from collections import namedtuple, defaultdict
import csv
from nyc_parking_ticket import ParkingSummonIterator, calculate_violations_by_make

class TestParkingSummonIterator(unittest.TestCase):

    def setUp(self):
        # Sample CSV data for testing
        self.csv_data = """Summons Number,Plate ID,Registration State,Plate Type,Issue Date,Violation Code,Vehicle Body Type,Vehicle Make,Violation Description
12345,ABC123,NY,ABC,01/01/2024,1,SEDAN,Toyota,Expired Meter
67890,XYZ789,NY,XYZ,01/02/2024,2,COUPE,Ford,No Permit
13579,DEF456,CA,DEF,01/03/2024,1,SEDAN,Toyota,No Permit
"""
        f = open('test_csvfile.csv','w')
        f.write(self.csv_data)
        f.close()
        self.iterator = ParkingSummonIterator('test_csvfile.csv')

    def test_iterator(self):
        summon = next(self.iterator)
        self.assertEqual(summon.Summons_Number, 12345)
        self.assertEqual(summon.Plate_ID, 'ABC123')
        self.assertEqual(summon.Issue_Date, datetime.strptime("01/01/2024", "%m/%d/%Y"))
        self.assertEqual(summon.Vehicle_Make, 'Toyota')
        
        summon = next(self.iterator)
        self.assertEqual(summon.Summons_Number, 67890)
        self.assertEqual(summon.Vehicle_Make, 'Ford')

    def test_calculate_violations_by_make(self):
        violations = calculate_violations_by_make(self.iterator)
        self.assertEqual(violations, [('Toyota', 2), ('Ford', 1)])

if __name__ == '__main__':
    unittest.main()
