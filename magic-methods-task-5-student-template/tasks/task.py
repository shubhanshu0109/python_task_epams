import os
import shutil
import tempfile

class TempDir:
    def __enter__(self):
        self.original_dir = os.getcwd()  # Save the current working directory
        self.temp_dir = tempfile.mkdtemp()  # Create a new temporary directory
        os.chdir(self.temp_dir)  # Change to the new temporary directory
        return self.temp_dir  # Optionally return the directory name

    def __exit__(self, exc_type, exc_value, traceback):
        os.chdir(self.original_dir)  # Change back to the original directory
        shutil.rmtree(self.temp_dir)  # Remove the temporary directory and all its contents

# Example usage
with TempDir() as temp_dir:
    print(f"Current working directory: {os.getcwd()}")
    # Perform actions in the temporary directory
print(f"Returned to directory: {os.getcwd()}")
