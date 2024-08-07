import os
import sys

class Config():
    def __init__(self):

        # Set target here
        self.company_name = ""
        # Recommended target url is about page
        self.url = ""
        self.target = f"{self.url}" # Add path if required 

        self.company_name_f = self.clean_filename(self.company_name)

        # Filepaths
        self.filepath = f"campaigns/{self.company_name_f}"
        self.strategy_filepath = f"{self.filepath}/strategy"
        self.company_profile_filepath = f"{self.filepath}/company-profile"
        self.simulation_filepath = f"{self.filepath}/simulations"
        self.landing_page_filepath = f"{self.filepath}/landing-pages"
        self.conversations_filepath = f"{self.filepath}/conversations"

        isExist = os.path.exists(self.strategy_filepath)
        if not isExist:
            os.makedirs(self.strategy_filepath)

        isExist = os.path.exists(self.company_profile_filepath)
        if not isExist:
            os.makedirs(self.company_profile_filepath)

        isExist = os.path.exists(self.simulation_filepath)
        if not isExist:
            os.makedirs(self.simulation_filepath)

        isExist = os.path.exists(self.landing_page_filepath)
        if not isExist:
            os.makedirs(self.landing_page_filepath)

        isExist = os.path.exists(self.conversations_filepath)
        if not isExist:
            os.makedirs(self.conversations_filepath)

        def create_file_if_not_exists(filename):
            # Check if the file already exists
            if not os.path.exists(filename):
                sys.exit(0)
            else:
                # File does not exist, create it by opening in write mode
                with open(filename, 'a') as file:
                    file.write('')  # Write an empty string just to create the file
