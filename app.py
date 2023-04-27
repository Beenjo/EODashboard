from flask_socketio import SocketIO
from flask import Flask, render_template, request
from threading import Lock
import datetime
import os
from random import random

"""
Background Thread
"""
thread = None
thread_lock = Lock()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'xr9sFMdCbarV8vWU'
socketio = SocketIO(app, cors_allowed_origins='*')


def get_current_datetime():
	return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def background_thread():
	print("Generating random sensor values")
	while True:
		dummy_sensor_value = round(random() * 100, 3)
		socketio.emit('updateSensorData', {'value': dummy_sensor_value, "date": get_current_datetime()})
		socketio.sleep(1)


@app.route('/')
def index():
	return render_template('index.html')


if __name__ == '__main__':
	app.run()
