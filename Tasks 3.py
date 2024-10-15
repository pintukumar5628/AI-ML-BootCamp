## 3. Create a Python program that uses a recursive function to calculate the total size of all files in a directory, including subdirectories. Use loops for directory traversal, logging for each step of the process, and exception handling to deal with permission issues or missing directories.
import os
import logging

# Configure logging
logging.basicConfig(filename='directory_size.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')


def calculate_directory_size(path):
    """
    Recursively calculates the total size of all files in the directory and its subdirectories.
    """
    total_size = 0
    try:
        # Traverse the directory using os.walk (for loops)
        for dirpath, dirnames, filenames in os.walk(path):
            logging.info(f"Accessing directory: {dirpath}")
            print(f"Accessing directory: {dirpath}")

            # Loop through each file in the directory
            for filename in filenames:
                file_path = os.path.join(dirpath, filename)
                try:
                    # Add the file size to the total
                    file_size = os.path.getsize(file_path)
                    total_size += file_size
                    logging.info(f"File: {file_path} - Size: {file_size} bytes")
                except OSError as e:
                    logging.error(f"Error accessing file: {file_path} - {e}")
                    print(f"Error accessing file: {file_path} - {e}")

    except PermissionError as e:
        logging.error(f"PermissionError: Unable to access directory: {path} - {e}")
        print(f"PermissionError: Unable to access directory: {path} - {e}")
    except FileNotFoundError as e:
        logging.error(f"FileNotFoundError: Directory not found: {path} - {e}")
        print(f"FileNotFoundError: Directory not found: {path} - {e}")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        print(f"Unexpected error: {e}")

    return total_size


if __name__ == "__main__":
    # Example: Specify the directory path you want to calculate the size of
    directory_path = input("Enter the directory path: ")
    total_size = calculate_directory_size(directory_path)
    print(f"Total size of '{directory_path}' is {total_size} bytes")
