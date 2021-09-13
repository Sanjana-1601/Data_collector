from flask import Flask, render_template,request
import pymongo
from pymongo import MongoClient
import json
from bson import json_util

app=Flask(__name__)
List=[]

cluster = pymongo.MongoClient('mongodb+srv://Sanjana:yes1234@cluster0.vvgoz.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db = cluster["data_collector"]
col = db["data_collection"]


@app.route('/', methods=["POST","GET"])
def first():
    name=request.form.get('name')
    company = request.form.get('company')
    email = request.form.get('email')
    return render_template("index.html") 


@app.route('/second', methods=["POST","GET"])
def second():
         info=request.form.get("name")
         print(info)
         return render_template("second.html")     
 

@app.route('/showd', methods=["POST","GET"])
def showd():
    info=request.form.get("info")
    col.insert({ "info": info })
    my_data = list(col.find({}))
    for y in my_data:
        my_dict = y
        List.append(my_dict['info'])
    abc=render_template("show.html")    
    l=len(List)
    return json.dumps(List[l-1], default=json_util.default) 
 
if __name__ == '__main__':
    app.run(debug=True)        
