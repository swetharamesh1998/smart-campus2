import paho.mqtt.client as Cli
import sqlite3
import time
import string
import random
global msg
broker = 'postman.cloudmqtt.com'
port = 10601
user = 'velofqbk'
password = 'uy4FH4uiHP8i'
client = Cli.Client('client2')
conn = sqlite3.connect('db.sqlite3')
msg = ''
cur = conn.cursor()


def verify(msg):
    pc = random.sample(string.ascii_uppercase+string.ascii_lowercase+string.digits, 8)
    passcode = ''.join(pc)
    cur.execute("SELECT passcode FROM student_entry WHERE uid=?;", (msg,))
    p2 = cur.fetchone()
    if(p2 is not None):
        p = "".join(p2)
    else:
        cur.execute('insert into student_entry(uid,passcode) values(?,?);', (msg, passcode,))
        conn.commit()
        p = passcode
    print(p + ' is the passcode')
    print('Publishing')
    client.publish("inTopic", payload=p)


def on_connect(client, userdata, flags, keys):
    print('Subscribing')
    client.subscribe("outTopic")
    time.sleep(2)


def on_message(client, userdata, message):
    msg = str(message.payload.decode('UTF-8'))
    print('Message received ', msg)
    verify(msg)


def on_publish(client, userdata, result):
    print('Published successfully')


client.on_connect = on_connect
client.on_message = on_message
client.on_publish = on_publish
client.connect(broker, port=port)
client.username_pw_set(user, password)
client.loop_forever()
client.disconnect()
conn.close()
