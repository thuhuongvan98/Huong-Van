import pymongo
from bson import ObjectId

hw = pymongo.MongoClient('mongodb://admin:admin@ds021182.mlab.com:21182/c4e',retryWrites=False)
db = hw['c4e']

#Exercise 3
post_collection = db['posts']
post_collection.insert_one({
    'title': 'C4E67',
    'author': 'Huong Van',
    'content': 'Hello mình sẽ cố gắng hiểu bài'
})

#Exercise 4
customers_collection = db['customers']
events = int(customers_collection.count_documents({'ref': 'events'}))
ads = int(customers_collection.count_documents({'ref': 'ads'}))
wom = int(customers_collection.count_documents({'ref': 'wom'}))

print('events: ',events)
print('ads: ',ads)
print('wom: ',wom)

from matplotlib import pyplot
pyplot.pie([events,ads,wom],labels=['events','ads','wom'],autopct='%.1f%%',shadow=True, explode=[0,0.1,0])
pyplot.axis('equal')
pyplot.title('REFERENCES')
pyplot.show()