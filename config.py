from dotenv import load_dotenv
import os
import phi.api

class Config:
    def __init__(self):
        load_dotenv()
        self.google_api_key = os.getenv("GOOGLE_API_KEY")
        self.phi_api_key = os.getenv("PHI_API_KEY")

    def setup_environment(self):
        os.environ["GOOGLE_API_KEY"] = self.google_api_key
        phi.api= self.phi_api_key