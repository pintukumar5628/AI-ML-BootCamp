## 2. Write a Python program that reads a file with complex structured data, processes each line using a loop, and logs any formatting errors or exceptions encountered. The function should handle cases like missing values or incorrect data formats, and log errors for review.
import logging

# Configure logging
logging.basicConfig(filename='data_processing.log', level=logging.ERROR,
                    format='%(asctime)s:%(levelname)s:%(message)s')

def process_line(line):
    """
    Processes a single line of structured data.
    Assumes that data is separated by commas and expects specific types in each field.
    """
    try:
        # Split the line into fields (assuming comma-separated values)
        fields = line.strip().split(',')

        # Check for missing fields
        if len(fields) != 4:
            raise ValueError(f"Expected 4 fields, but got {len(fields)} fields")

        # Extract and validate each field
        name = fields[0]
        age = int(fields[1])  # Should be an integer
        salary = float(fields[2])  # Should be a float
        department = fields[3]  # Should be a string

        # Process the valid data (for example, just print it here)
        print(f"Processed: Name={name}, Age={age}, Salary={salary}, Department={department}")

    except ValueError as e:
        logging.error(f"ValueError while processing line: {line.strip()} - {e}")
        print(f"Error processing line: {e}")
    except Exception as e:
        logging.error(f"Unexpected error while processing line: {line.strip()} - {e}")
        print(f"Unexpected error: {e}")

def process_file(filename):
    """
    Reads and processes each line of the file.
    Logs any errors encountered during processing.
    """
    try:
        with open(filename, 'r') as file:
            for line_num, line in enumerate(file, start=1):
                if line.strip():  # Skip empty lines
                    print(f"Processing line {line_num}: {line.strip()}")
                    process_line(line)
    except FileNotFoundError as e:
        logging.error(f"FileNotFoundError: File '{filename}' not found")
        print(f"Error: File '{filename}' not found")
    except Exception as e:
        logging.error(f"Unexpected error while reading file: {filename} - {e}")
        print(f"Unexpected error while reading file: {e}")

if __name__ == "__main__":
    # Example: Assume the file is named 'data.txt' and has complex structured data
    process_file('tasks1.py')
