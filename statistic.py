import pprint
from pymongo import MongoClient
from bson.son import SON
# #
client = MongoClient(None)
db = client.test
# # print(db.hotels.find_one())
# # print('!')

print('Total count of all available hotels found: {}'.format(db.hotels.count()), end='\n\n')

print('Arrange the list by prefecture:', end='\n\n')
pipeline = [
    {"$group": {"_id": "$prefecture", "count": {"$sum": 1}}},
    {"$sort": SON([("count", -1), ("_id", -1)])}
]
pprint.pprint(list(db.hotels.aggregate(pipeline)))
print('\n')
print('Arrange the list by hotel type:', end='\n\n')
pipeline = [
    {"$group": {"_id": "$type", "count": {"$sum": 1}}},
    {"$sort": SON([("count", -1), ("_id", -1)])}
]
pprint.pprint(list(db.hotels.aggregate(pipeline)))