#!/usr/bin/env python
from flask import Flask, request, jsonify
from flaskext.mysql import MySQL
import MySQLdb
from flask_restful import Resource, Api
import ConfigParser
import json
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify, request

app = Flask(__name__)

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'mysql'
app.config['MYSQL_DATABASE_DB'] = 'ITS'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="mysql",
                     db="ITS")

cur = db.cursor()
db.autocommit(True)
@app.route("/")
def index():
  return "You have reached the site."

@app.route("/locations")
def locations():
  query="SELECT * FROM Device_Location"
  cur.execute(query)
  locations = [dict(DeviceId=row[0], Location=row[1]) for row in cur.fetchall()]
  return jsonify(locations)

@app.route("/sensors/")
def sensors():
#JSONIFY THE sensors current value;
    query="SELECT * from Device"
    cur.execute(query)
    locations = [dict(DeviceId=row[0], DeviceName=row[1]) for row in cur.fetchall()]
    return jsonify(locations)

#Pruthvi->Server (single)
@app.route("/sensors/<sensor_id>",methods=["POST"])
def sensor_id(sensor_id):
  if request.method=="POST":
      print "sensor_id",sensor_id;
      data = request.data
      print request.data
      DeviceName=request.data['DeviceName']
      Value=request.data['Value']
      Datetime=request.data['datetime']
      query1="INSERT INTO Device_Value (DeviceId, Value, recordtime) VALUES (%d,%f,%d)"%(sensor_id,Value,Datetime)
      cur.execute(query1)
      query2="INSERT INTO Device (DeviceId,DeviceName) VALUES (%d,%s)"%(sensor_id,DeviceName)
      cur.execute(query2)
      return "Values entered into the database"

#Chaitu -> Server
@app.route("/sensors/<int:sensor_id>/ON",methods=["POST"])
def sensor_ON(sensor_id):
  if request.method=="POST":
      query="INSERT INTO Device_status (DeviceId,Status) VALUES(%d,%s) ON DUPLICATE KEY UPDATE"%(sensor_id,"1")
      #query="UPDATE Device_status SET Status=1 where DeviceId=%s"%(sensor_id)
      cur.execute(query)
      db.commit()
      return "The request has been processed."

#Chaitu->Server
@app.route("/sensors/<int:sensor_id>/OFF",methods=["POST"])
def sensor_OFF(sensor_id):
    if request.method=="POST":
        query="INSERT INTO Device_status (DeviceId,Status) VALUES(%d,%s) ON DUPLICATE KEY UPDATE"%(sensor_id,"0")
        #query="UPDATE Device_status SET Status=0 where DeviceId=%s"%(sensor_id)
        cur.execute(query)
        return "Entered into the database"

#Server ->Chaitu
@app.route("/sensors_json_all",methods=["GET"])
def sensors_json_all():
     query="SELECT * FROM Device_Value"
     cur.execute(query)
     sensors = [dict(DeviceId=row[0], Value=row[1], recordtime=row[2], ) for row in cur.fetchall()]
     return jsonify(sensors)

#Server->Pruthvi
@app.route("/<sensor_id>/status",methods=["GET"])
def sensor_status(sensor_id):
    query="SELECT Status FROM Device_status where DeviceId=%s"%(sensor_id)
    cur.execute(query)
    State = [dict(Status=row[0],) for row in cur.fetchall()]
    return jsonify(State)

if __name__=="__main__":
  app.run(debug=True)
