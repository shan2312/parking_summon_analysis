**README.md**

```markdown
# Parking Summon Analysis

## Overview

This project provides a lazy iterator for parsing parking summons data and calculating the number of violations by car make. It is designed to handle large datasets efficiently by using lazy evaluation.

## Requirements

- Python 3.6 or higher
- No additional external libraries are required other than the standard Python library.

## Usage

### 1. Create a Lazy Iterator

The `ParkingSummonIterator` class reads a CSV file and provides an iterator that returns named tuples representing each row of the data.

**Example Usage:**

```python
from parking_summon import ParkingSummonIterator

filepath = 'path_to_your_csv_file.csv'
iterator = ParkingSummonIterator(filepath)

for summon in iterator:
    print(summon)
```

### 2. Calculate Violations by Car Make

The `calculate_violations_by_make` function takes an instance of `ParkingSummonIterator` and returns a sorted list of tuples containing the car make and the count of violations.

**Example Usage:**

```python
from parking_summon import ParkingSummonIterator, calculate_violations_by_make

filepath = 'path_to_your_csv_file.csv'
iterator = ParkingSummonIterator(filepath)
violations = calculate_violations_by_make(iterator)

for make, count in violations:
    print(f'{make}: {count} violations')
```

## Test Cases

To run the test cases, you need to have the `unittest` framework. The provided test cases include:

- Iteration over the CSV data to ensure correct parsing.
- Calculation of violations by car make to ensure correct functionality.

**To run tests:**

```bash
python -m unittest test_parking_summon.py
```

## Notes

- Ensure that your CSV file follows the format expected by `ParkingSummonIterator`.
- The code assumes that all fields in the CSV file are correctly formatted as per the data types specified.

## License

This project is licensed under the MIT License.
```

### Notes:

1. **Test Cases**: The tests use `StringIO` to simulate file input. For more robust testing, you could use actual files or mock external dependencies.
2. **README**: This file provides a high-level overview and instructions. Adjust file paths and details as per your actual setup.

Let me know if you need further modifications or additional information!