# Heliverse: Selenium Automation for SauceDemo Application

This README file provides a comprehensive overview of the Selenium-based automation project for testing the SauceDemo application. The project covers various test scenarios, including login functionality, product interactions, sorting, the checkout process, and navbar features.

## Getting Started

### Prerequisites

Before running the tests, make sure you have Python installed on your system. You can download and install Python from the official website: [python.org](https://www.python.org/).

### Installing Dependencies

To install all the required Python modules for the project, follow these steps:

1. Clone the repository to your local machine.
2. Open a terminal or command prompt and navigate to the project root directory.
3. Run the following command to install all the dependencies listed in the `requirements.txt` file:

   ```bash
   pip install -r requirements.txt
   ```

   This command will ensure that all the necessary Python packages are installed before you proceed with running the tests.

### Checking Installed Modules

After installing the required modules, you can verify whether all necessary dependencies are installed by using the `pip list` command. This command will display a list of all the Python packages currently installed in your environment.

Here’s how to check if the modules from `requirements.txt` are installed:

1. **Run the `pip list` Command:**
   ```bash
   pip list
   ```

2. **Compare Installed Modules:**
   - The command will output a list of installed modules along with their versions.
   - You can manually compare this list with the contents of your `requirements.txt` file to ensure that all required modules are installed.

3. **Troubleshooting:**
   - If any module is missing, you can install it individually by using the `pip install <module_name>` command.

By following these steps, you can ensure that your local environment is properly set up with all the necessary dependencies before running the automation tests.

## Project Overview

### Selenium Automation Workflow

To ensure code maintainability and clarity, the project is organized into a structured directory. Here’s an overview of the key components:

1. **Project Root:**
   - The project root directory contains the primary automation codebase.
  
2. **Directory Structure:**
   - **`Locators`**: Contains all web element locators used throughout the project.
   - **`Functions`**: Houses reusable functions for different automation tasks.
   - **`Tests`**: Contains the test cases that execute various scenarios within the SauceDemo application.
     - **`Logs`**: Stores log files for each test case in a timestamped format.
     - **`Report`**: Contains an HTML report that displays the test case results in a browser-friendly format.
       - *Note*: If the `Logs` or `Report` folders do not exist, they are automatically created by the `conftest.py` script.
   - **`Utils`**: Includes utility functions and helper scripts to support the automation framework.
  
3. **Configuration Files:**
   - **`config.ini`**: Defines constants and values used across the project.
   - **`pytest.ini`**: Contains configuration for pytest, including markers for suite creation. 
     - *Note*: This file can be modified based on user requirements.

4. **Other Key Files:**
   - **`conftest.py`**: Initializes the automation workflow, including setting up and tearing down WebDriver instances.
   - **`requirements.txt`**: Lists the Python packages necessary to run the automation code. Ensure these dependencies are installed before running the tests.

## Log Files

Log files are generated for each test case, recording detailed execution logs. These logs are stored in the `Logs` folder and help in diagnosing test failures.

## Running Selected Test Suites

The `run_selected_suites.py` script enables running specific test suites or test cases, which is helpful when dealing with a large number of tests. The test suites to be executed are defined in the `suite_config.json` file.

### Commands to Run Tests

- **Run All Test Cases:**
  ```bash
  pytest
  ```
  This command runs all the test cases in the project.

- **Run a Specific Test Suite:**
  ```bash
  pytest -m <suite_name>
  ```
  This command runs a specific test suite by referencing the suite name, which is marked in the `pytest.ini` file.

## Generating HTML Reports

To generate HTML reports, the `pytest_configure` method is used in the `conftest.py` file. This method automatically creates an HTML report each time a test is run, and saves the report in the `Report` folder under the `Tests` directory.

### Note on Manual HTML Report Generation

You can also generate the HTML report manually using the following commands:

- **To run all tests and generate an HTML report:**
  ```bash
  pytest --html={report_file_name} --self-contained-html
  ```

- **To run specific test suites and generate an HTML report:**
  ```bash
  pytest -m <suite_name> --html={report_file_name} --self-contained-html
  ```

**Important Note:** One of the disadvantages of this method is that the HTML file will always be created in the directory where this command is executed. For example, if you execute the command in the root directory, the HTML report will be created in the root directory instead of the `Report` folder. To avoid this, the `pytest_configure` method in the `conftest.py` file ensures that the HTML report is always created in the `Report` folder, regardless of where the command is executed. Additionally, this method eliminates the need to use the `--html={report_file_name} --self-contained-html` option, simplifying the command.

## Observations During Testing

The SauceDemo application was tested with various user profiles. Below are the key observations for each username:

### Username: `standard_user`

- **Login**: Successful
- **Glitch**: No
- **Pictures of Products**: All images are visible.
- **Alignment of Data**: Correct
- **Products Clickable**: All items are clickable.
- **Sorting of Products**: All sorting options work as expected.
- **Product Details on Main Page**: Correct product is displayed.
- **Navbar Functionality**: Working correctly.
- **Checkout Process**: All fields work correctly.
- **Logout**: Successful

### Username: `locked_out_user`

- **Login**: Unsuccessful
- **Glitch**: No
- **Pictures of Products**: Not available (due to failed login)
- **Alignment of Data**: Not applicable
- **Products Clickable**: No
- **Sorting of Products**: Not applicable
- **Product Details on Main Page**: Not applicable
- **Navbar Functionality**: Not applicable
- **Checkout Process**: Not applicable
- **Logout**: Successful

### Username: `problem_user`

- **Login**: Successful
- **Glitch**: No
- **Pictures of Products**: Not visible on the homepage but appear after clicking on a product.
- **Alignment of Data**: Correct
- **Products Clickable**: Only a few items are clickable.
- **Sorting of Products**: Sorting options are non-functional.
- **Product Details on Main Page**: Incorrect product is displayed (e.g., clicking on Sauce Labs Backpack shows Sauce Labs Fleece Jacket).
- **Navbar Functionality**: Working correctly.
- **Checkout Button**: Issues with field behavior (e.g., the last name field overwrites the first name field).
- **Continue Button**: Not working due to field validation issues.
- **Finish Button**: Not applicable as the continue button fails.
- **Logout**: Successful

### Username: `performance_glitch_user`

- **Login**: Successful
- **Glitch**: Yes, reloading is slow.
- **Pictures of Products**: All images are visible.
- **Alignment of Data**: Correct
- **Products Clickable**: All items are clickable.
- **Sorting of Products**: All sorting options work as expected.
- **Product Details on Main Page**: Correct product is displayed.
- **Navbar Functionality**: Working correctly.
- **Checkout Process**: All fields work correctly.
- **Logout**: Successful

### Username: `error_user`

- **Login**: Successful
- **Glitch**: No
- **Pictures of Products**: All images are visible.
- **Alignment of Data**: Correct
- **Products Clickable**: Only a few items are clickable.
- **Sorting of Products**: Sorting options are non-functional.
- **Product Details on Main Page**: Correct product is displayed.
- **Navbar Functionality**: Working correctly.
- **Checkout Button**: Last name field remains empty (a bug).
- **Continue Button**: Working despite the last name field being empty (another bug).
- **Finish Button**: Not clickable due to the last name field issue.
- **Logout**: Successful

### Username: `visual_user`

- **Login**: Successful
- **Glitch**: No
- **Pictures of Products**: All images are visible except Sauce Labs Backpack on the homepage.
- **Alignment of Data**: Misaligned elements (e.g., Cart button, Hamburger Menu).
- **Products Clickable**: All items are clickable.
- **Sorting of Products**: Sorting appears to be incorrect due to price value inconsistencies (sorted based on original prices).
- **Product Details on Main Page**: Correct product is displayed with original pricing.
- **Navbar Functionality**: Prices on the main page change with every click.
- **Checkout Process**: All fields work correctly.
- **Logout**: Successful

---
