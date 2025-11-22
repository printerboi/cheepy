# First, make sure to install the package:
# pip install python-dotenv

from dotenv import load_dotenv
import os


class Config:

    def __init__(self, env_file=".env"):
        load_dotenv(dotenv_path=env_file)

        self.user = os.getenv("BASIC_USER")
        self.password = os.getenv("BASIC_PASSWORD")