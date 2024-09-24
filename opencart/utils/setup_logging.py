import logging
import os
import datetime


# Create the session folder during the import
session_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
session_folder = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'logs',
                              f"session_{session_time}")
try:
    os.makedirs(session_folder, exist_ok=True)
except OSError as e:
    raise OSError(f"Failed to create session folder '{session_folder}': {e}")


def setup_logging(test_file_name):
    """
    Sets up logging for each test, creating a unique log file for each test run.

    :param test_file_name: The name of the test file for which the log is being created.
    :return: A tuple of the logger and the path to the test log directory.
    :raises OSError: If the log directory cannot be created.
    """
    test_name = os.path.splitext(os.path.basename(test_file_name))[0]

    # Create a directory for the test's logs
    test_log_dir = os.path.join(session_folder, test_name)
    try:
        os.makedirs(test_log_dir, exist_ok=True)
    except OSError as e:
        raise OSError(f"Failed to create test log directory '{test_log_dir}': {e}")

    log_file_name = os.path.join(test_log_dir, f"{test_name}.log")

    logger = logging.getLogger(test_name)
    logger.setLevel(logging.ERROR)

    # Remove any existing handlers to avoid duplication
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)

    # Add a file handler for the test-specific log
    file_handler = logging.FileHandler(log_file_name)
    file_handler.setLevel(logging.ERROR)

    # Format log messages
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger, test_log_dir
