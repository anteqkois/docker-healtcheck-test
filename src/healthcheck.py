import sys
import time
import pymongo
from utils import getMongoClient

try:
	# Connect to MongoDB
	client = getMongoClient("target", 'order_book4')
	db = client['order_book4']
	collection = db["order_book_ranking"]
	
	# Get the latest document based on the 'ts' field
	latest_doc = collection.find_one({}, sort=[("ts", pymongo.DESCENDING)])
	print(latest_doc)

	if latest_doc is None:
			print("No documents found in the collection")
			sys.exit(1)  # Failure

	# Get the current time in Unix timestamp format
	current_ts = int(time.time())

	# Check if the last document's 'ts' is older than 4 minutes
	if current_ts - latest_doc["ts"] > 4 * 60:
			print(f"Healthcheck failed: Last document is too old (ts={latest_doc['ts']})")
			sys.exit(1)  # Failure

	print("MongoDB is up and latest document is recent")
	sys.exit(0)  # Success

except Exception as e:
	print(f"Healthcheck failed: {e}")
	sys.exit(1)  # Failure