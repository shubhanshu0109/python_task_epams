import os

class Cd:
    def __init__(self, path):
        if not os.path.isdir(path):
            raise ValueError("The passed directory does not exist or is not a directory.")
        self.path = path
        self.saved_path = None

    def __enter__(self):
        self.saved_path = os.getcwd()
        os.chdir(self.path)

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.chdir(self.saved_path)