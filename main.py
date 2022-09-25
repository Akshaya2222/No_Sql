import pymongo

DEFAULT_CONNECTION_URL = "mongodb://localhost:27017"
DB_NAME = "pybron_1"
client = pymongo.MongoClient(DEFAULT_CONNECTION_URL)

database = client['DB_NAME']

record = {
    'company_name': "pybron",
    "product": "Affordable_ML",
    'course_offered': "MACHINE learning for Data Scientiest",
    "trainer_name": "rajesh"

}
collection_name = "pybron_product"
collection = database[collection_name]

collection.insert_one(record)