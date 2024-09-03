import os
from utils.helpers import Utils

# Specify the path to the configuration file
config_file_path = "suites_config.json"

# Specify the name and path for the HTML report
report_file_path = os.path.join("tests", "Report" ,"report.html")

Utils.run_selected_suites(config_file_path, report_file_path)