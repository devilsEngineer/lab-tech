#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  2 13:03:42 2019

@author: ananthu
"""

from flask import Flask,request
from pymongo import MongoClient
from gevent.pywsgi import WSGIServer
from flask import jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)    

client = MongoClient("mongodb://127.0.0.1:27017")
db = client.lab                           #database  
users = db.customer                       #collection name  
 
@app.route("/listAllCustomers", methods=['GET'])  
def lists ():  
    #List all users
    users_list = users.find({}) 
    doc=[]
    for document in users_list:
        document.pop("_id")
        doc.append(document)
    return jsonify({"Result":doc})
    
@app.route("/addCustomer", methods=['POST'])  
def create ():  
    #Adding a user 
    content = dict(request.get_json())
    print(content)
    name=content['name']  
    dob=content['dob']
    phone=content['phone'] 
    cid=name+"_"+dob+"_"+phone
    print(cid)
    content["cid"]=cid
    print(content)
    users.update_one({'cid':content['cid']},{'$set':content},True)
    return jsonify("Success") 

@app.route("/remove", methods=['DELETE'])  
def remove ():  
    #Deleting a user 
    key=request.values.get("cid")  
    users.remove({"cid":key})  
    return("OK") 

@app.route("/search", methods=['GET'])  
def search():  
    #Searching a user with various references
    refer=request.values.get("refer") 
    key=request.values.get("key")   
    users_list = users.find({refer:key})
    doc=[]
    for document in users_list:
        document.pop("_id")
        doc.append(document)
    return jsonify({"Result":doc})

@app.route("/getCustomer", methods=['GET'])
def user_details():
    #Detail of a particular customer
    name=request.values.get("name")
    dob=request.values.get("dob")
    phone=request.values.get("phone") 
    cid=name+"_"+dob+"_"+phone
    users_list = users.find({"cid":cid})
    doc=[]
    for document in users_list:
        document.pop("_id")
        doc.append(document)
    return jsonify({"Result":doc})  


if __name__ == "__main__":
    http_server = WSGIServer(('', 8007), app)
    http_server.serve_forever()
