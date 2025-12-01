from azure.cosmos import CosmosClient, PartitionKey, exceptions
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

COSMOS_URI = os.getenv("COSMOS_URI")
COSMOS_KEY = os.getenv("COSMOS_KEY")
DATABASE_NAME = os.getenv("DATABASE_NAME")
CONTAINER_NAME = os.getenv("CONTAINER_NAME")

def connect_cosmos():
    try:
       
        client = CosmosClient(COSMOS_URI, credential=COSMOS_KEY)
        print("✔ Connected to Cosmos DB")

   
        database = client.create_database_if_not_exists(id=DATABASE_NAME)

     
        container = database.create_container_if_not_exists(
            id=CONTAINER_NAME,
            partition_key=PartitionKey(path="/branch"),
            offer_throughput=400
        )

        print("✔ Database & container ready")
        return container

    except exceptions.CosmosHttpResponseError as e:
        print("❌ Error connecting to Cosmos DB:", e)
        return None


if __name__ == "__main__":
    container = connect_cosmos()
