# helpers.py
import configparser
import os
import logging
import inspect
import json
import subprocess

class Utils:
    def load_config():
        config = configparser.ConfigParser()
        config_path = os.path.join(os.path.dirname(__file__), '..', 'config.ini')
        config.read(config_path)
        return config
    
    @staticmethod
    # DEBUG --> INFO --> WARNING --> ERROR --> CRITICIAL 
    def custom_logger(logLevel = logging.WARNING, log_file_name="automation.log"):
       
        # Set the logger name as the function name where it is called
        logger_name = inspect.stack()[1][3]
        
        # Create logger
        logger = logging.getLogger(logger_name)
        logger.setLevel(logLevel)

        # Clear previous handlers
        if logger.hasHandlers():
            logger.handlers.clear()

        # Define the log file path
        log_folder_path = os.path.join(os.path.dirname(__file__), '..', 'Tests', 'Logs')
        if not os.path.exists(log_folder_path):
            os.makedirs(log_folder_path)
        
        log_file_path = os.path.join(log_folder_path, log_file_name)

        # Create file handler and set the log level 
        fh = logging.FileHandler(log_file_path, mode='w')
        
        # Create formatter - how you want your logs to be formatted 
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        
        # Add formatter to file handler 
        fh.setFormatter(formatter)
        
        # Add handler to logger 
        logger.addHandler(fh)
        return logger

    def run_selected_suites(config_file, report_file):
    # Load the configuration file
        with open(config_file, "r") as f:
            config = json.load(f)
            suites = config.get("suites_to_run", [])
            
            # List to collect valid test suite paths
            valid_suites = []

            for suite in suites:
                if os.path.exists(suite):
                    print(f"Adding test suite: {suite}")
                    valid_suites.append(suite)
                else:
                    print(f"Test suite {suite} does not exist.")

            if valid_suites:
                print(f"Running {len(valid_suites)} test suites and generating HTML report.")
                result = subprocess.run(
                    ["pytest", *valid_suites, f"--html={report_file}", "--self-contained-html"],
                    capture_output=True,
                    text=True
                )
                print(result.stdout)
                if result.returncode != 0:
                    print("Some test suites failed.")
            else:
                print("No valid test suites to run.")