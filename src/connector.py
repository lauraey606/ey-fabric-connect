import os
from dotenv import load_dotenv

load_dotenv()

class FabricClient:
    def __init__(self):
        self.workspace_id = os.getenv('FABRIC_WORKSPACE_ID')
    
    def connect(self):
        return True