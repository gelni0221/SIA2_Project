import os
#pip install python-dotenv

from dotenv import load_dotenv

# FOR LOADING .ENV FILE FOR THE STEAM API KEY
load_dotenv()

# TO ACCESS THE API KEY
steam_api_key = os.getenv("STEAM_API_KEY")

