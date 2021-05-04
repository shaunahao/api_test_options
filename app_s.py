#!/usr/bin/env python
#!coding:utf-8
from flask import Flask, jsonify
from flask_restful import  Api,Resource,reqparse
app=Flask(__name__)
api=Api(app)

class LoginView(Resource):
   def get(self):
      return {'status':0,'msg':'ok','data':'stage - this is a login page'}
   
   def post(self):
       parser=reqparse.RequestParser()
       parser.add_argument('username', type=str, required=True, help='username is wrong')
       parser.add_argument('password',type=str, required=True, help='password is wrong') 
       parser.add_argument('age', required=True, type=int,help='age must be int') 
       parser.add_argument('sex',type=str,help='sex is wrong',choices=['F','M']) 
       args=parser.parse_args()
       return jsonify(args)

api.add_resource(LoginView,'/loginstage/',endpoint='loginstage')

if __name__ == '__main__':
   app.run(host="localhost", port=8000, debug=True)
