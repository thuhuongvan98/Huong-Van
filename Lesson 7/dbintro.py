import pymongo
from bson import ObjectId

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['c4e']

customer_collection = db['customer']
customer_collection.insert_one({
    'name' : 'Huong',
    'age' : 21,
    'address' : 'HBT'
})

#...insert_many(list)
#list = [...]

data1 = customer_collection.find({'name' : 'Nhi'})
data2 = customer_collection.find({'age': {'$lt' : '18'}}) #find record with age < 18 (little than), >18 (greater than)
#find_one: lấy thằng đầu tiên theo thứ tự
data3 = customer_collection.find_one({'_id': ObjectId("5e551ea097cb7942b03869f3")})
# for customer in data3:
#     print(customer)

print(data3)

customer_collection.update_one(
    {
        '_id': ObjectId("5e551ea097cb7942b03869f3")
    },
    {   
        '$set': {
            'name': 'Không phải con điên'
        }   
    }
)

customer_collection.delete_one({'_id': ObjectId("5e551ea097cb7942b03869f3")})

from faker import Faker

fake = Faker('el.GR')

# x = customer_collection.find()
# for i in x:
#     customer_collection.delete_one({'_id' : i['_id']})

for a in range(100):
    customer_collection.insert_one(
        {
            'name': fake.name(),
            'job': fake.job(),
            'address': fake.address(),
            'phone number': fake.phone_number()
    })