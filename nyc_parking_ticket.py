# Create lazy iterator that returns namedtuple of each row. Dtype should be appropriate.
# Number of violations by car make
##### Goal 1
# Create a lazy iterator that will return a named tuple of the data in each row. 
# The data types should be appropriate - i.e. if the column is a date, 
# you should be storing dates in the named tuple, if the field is an integer, then it should be stored as an integer, etc.
##### Goal 2
# Calculate the number of violations by car make.
##### Note:
# Try to use lazy evaluation as much as possible - it may not always be possible though! That's OK, as long as it's kept to a minimum.



from collections import namedtuple, defaultdict
import csv
from datetime import datetime

class ParkingSummonIterator:
    def __init__(self, filepath: str) -> None:
        """
        Constructor for ParkingSummonIterator class

        Args:
            filepath (string): path to file containing summons data
        """
        self._file = open(filepath, mode = 'r', newline = '\n', encoding='utf-8')
        self._reader = csv.DictReader(self._file, delimiter=',', quotechar='"')
        self.type_map = {'Summons Number': int, 'Plate ID': str, 'Registration State':str, 'Plate Type':str, 'Issue Date':lambda x: datetime.strptime(x, "%m/%d/%Y"), 'Violation Code':int, 'Vehicle Body Type':str, 'Vehicle Make':str, 'Violation Description':str}
        self.Summon = namedtuple('Summon', [name.replace(" ", "_") for name in self._reader.fieldnames])

    def __iter__(self):
        """Iter functions

        Returns:
            ParkingSummonIterator: Returns an iterator for ParkingSummonIterator class
        """
        return self
    
    def __next__(self):
        """Returns next element of iterator

        Returns:
            namedtuple: namedtuple containing all the details of summon
        """
        try:
            row = next(self._reader)
            row = {name: self.type_map[name](value) for name, value in row.items()}
            return self.Summon(*list(row.values()))
        except StopIteration:
            self._file.close()
            raise

def calculate_violations_by_make(summon_iterator: ParkingSummonIterator):
    """Calculates violation by vehicle make

    Args:
        summon_iterator (ParkingSummonIterator): Object of class ParkingSummonIterator

    Returns:
        dict: Dictionary containing count of violations by make
    """
    car_make_to_violations = defaultdict(int)
    for summon in summon_iterator:
        car_make_to_violations[summon.Vehicle_Make] += 1

    return sorted(list(car_make_to_violations.items()), key = lambda x: x[1], reverse = True)
