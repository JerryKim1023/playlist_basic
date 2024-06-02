from pymongo import MongoClient
client = MongoClient('mongodb+srv://ecec1023:Ljx10jeUZF0dGHIW@movies.aivdll0.mongodb.net/movies?retryWrites=true&w=majority&appName=movies')
db = client.movies

# 저장 - 예시

doc = {'name':'bobby','age':21}
db.users.insert_one(doc)

# 한개 찾기 - 예시
user = db.users.find_one({'name':'booby'})

# 여러개 찾기 - 예시 ( _id 값은 제외하고 출력)
all_users = list(db.users.find({},{'_id':False}))

# 바꾸기 - 예시
db.users.update_one({'name':'bobby'},{'$set':{'age':19}})

# 지우기 - 예시
db.users.delete_one({'name':'bobby'})