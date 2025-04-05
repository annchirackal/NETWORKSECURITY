
from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
mongo_db_url = os.getenv("MONGO_DB_URL")

uri = mongo_db_url 

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)