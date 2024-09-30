# Sauce Demo Test Automation Framework

This framework answers the test automation coding challenge:

- Develop a test script using a testing framework of your choice to automate the following scenario:
  - Navigate to an e-commerce website.
  - Search for a specific product.
  - Add the product to the cart.
  - Proceed to checkout.
- Ensure the script includes appropriate assertions to validate each step.
- The test script should handle dynamic elements and varying data inputs.

## Dependencies

1. Python 3.11+ installed

## How to Install the dependencies

1. Clone the repo to the local computer
2. Extract the repo and navigate into the project folder
3. Open a terminal in the project folder:
   - For Windows 11: right-click in the project folder and click `Open in terminal`
4. Run the command `pip install -r requirements.txt`
5. Or:
   - Install pipenv: run the command `pip install pipenv`
   - Create a .venv folder in the project folder: `mkdir .venv`
   - Run the command `pipenv install` to create an environment and install dependencies in the pipfile

## How to run the script

1. Open the terminal in the project folder
2. Run the command `python test.py`
3. After the script has finished running, open the test_logs.log file to view the logs
