import paho.mqtt.client as Cli
import sqlite3
import time
import string
import random
from datetime import datetime
broker = 'postman.cloudmqtt.com'
port = 10601
user = 'velofqbk'
password = 'uy4FH4uiHP8i'
client = Cli.Client('client2')
conn = sqlite3.connect('db.sqlite3')
cur = conn.cursor()


def add(msg):
    ls = msg.split(',')
    cur.execute('insert into student_checkin(uid,mid,checkInTime) values(?,?,?);', (ls[0], ls[1], datetime.now(),))



def on_connect(client, userdata, flags, keys):
    print('Subscribing')
    client.subscribe("checkIn")
    time.sleep(2)


def on_message(client, userdata, message):
    msg = str(message.payload.decode('UTF-8'))
    print('Message received ', msg)
    add(msg)
    conn.commit()


client.on_connect=on_connect
client.on_message=on_message
client.username_pw_set(user, password)
client.connect(broker, port=port)
client.loop_forever()
