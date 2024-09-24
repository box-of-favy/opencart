Project: OpenCart Automation
Author: Olya Osmatescu

About the Project

This project is part of my portfolio and represents automation testing for an e-commerce platform based on OpenCart. The project is freely distributed and can be used as a learning resource or as a foundation for your own test automation projects.

Requirements

To run the tests properly, you will need to:

Set up a Docker container with OpenCart. The scripts for the container are located in the docker/opencart directory.
Ensure that all dependencies from the requirements.txt file are installed.
How to Run the Tests

Clone the repository:
git clone [<repository-url>](https://github.com/box-of-favy/opencart)

Navigate to the project folder:
cd <project-folder>

Start the Docker container:
docker-compose up -d

Run the tests using the following command:
pytest

Logging
All test logs are saved in the opencart/logs directory. Ensure that this folder is writable before running tests.

Notes
All tests have been verified to work and pass successfully.
The project includes logging functionality to track test executions and errors.
