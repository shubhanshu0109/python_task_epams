import datetime
import time
from contextlib import ContextDecorator


class LogFile(ContextDecorator):
    def __init__(self, log_file_name):
        self.log_file_name = log_file_name

    def __enter__(self):
        self.start_time = datetime.datetime.now()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        end_time = datetime.datetime.now()
        execution_time = end_time - self.start_time
        error_info = f"{exc_value}" if exc_value else "None"

        log_message = (
            f"Start: {self.start_time.strftime('%Y-%m-%d %H:%M:%S.%f')} | "
            f"Run: {execution_time} | "
            f"An error occurred: {error_info}\n"
        )

        with open(self.log_file_name, 'a') as log_file:
            log_file.write(log_message)

        # If an exception occurred, re-raise it
        return not exc_type  # Return False to propagate the exception


# Example usage:

@LogFile('my_trace.log')
def some_func():
    print("This is a test function.")
    time.sleep(1)


@LogFile('my_trace.log')
def function_with_error():
    return 1 / 0  # This will cause a ZeroDivisionError


# Running the functions to generate log entries
some_func()

try:
    function_with_error()
except ZeroDivisionError:
    pass
