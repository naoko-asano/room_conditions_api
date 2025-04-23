from flask import Flask, jsonify
import board
import busio
import adafruit_sht31d

app = Flask(__name__)

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_sht31d.SHT31D(i2c)

@app.route("/")
def index():
    try:
        temperature = round(sensor.temperature, 1)
        humidity = round(sensor.relative_humidity, 1)
    except Exception:
        temperature = '???'
        humidity = '???'
    return jsonify({ 'temperature': temperature, 'humidity': humidity })
