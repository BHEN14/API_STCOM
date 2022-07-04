
from flask import Flask
import pymongo


app = Flask(__name__)

db = pymongo.MongoClient("mongodb+srv://root:root@students.lvpkb.mongodb.net/?retryWrites=true&w=majority")
coll = db["stcom"]
@app.route('/')
def hello_world():
  return 'Hello World'


if __name__ == '__main__':
  app.run()
