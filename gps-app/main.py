import serial
import pynmea2 as nmea
import threading
from flask import Flask, jsonify

ser = serial.Serial("COM5", 9600, timeout=1)
latest = {"fix": False, "lat": None, "lon": None,
          "alt": None, "sats": 0, "hdop": None}

def findDD(NMEA_Format, direction):
    mult =1
    if(direction == "S"):
        mult =-1
    elif(direction == "W"):
        mult = -1
    dot =NMEA_Format.find(".")
    degrees =NMEA_Format[:dot -2]
    minutes =NMEA_Format[dot - 2:]
    
    return round((mult * (int(degrees) + (float(minutes)/60))), 5)

def gps_reader():
    while True:
        line =ser.readline().decode("ascii", errors ="ignore").strip()
    
    
        try:
            msg =nmea.parse(line)
        except nmea.ParseError:
            continue
    
        if isinstance(msg, nmea.GGA):
            latest["sats"] = int(msg.num_sats or 0)
            if not msg.gps_qual:
                latest["fix"] =False
            else:
                latest["fix"] =True
                latest["lat"] =findDD(msg.lat, msg.lat_dir)
                latest["lon"] =findDD(msg.lon, msg.lon_dir)
                latest["alt"] =msg.altitude
                latest["hdop"] =float(msg.horizontal_dil)

app = Flask(__name__)

@app.route("/api/gps")
def api_gps():
    return jsonify(latest)

@app.route("/")
def index():
    return app.send_static_file("index.html")

if __name__ == "__main__":
    threading.Thread(target=gps_reader, daemon =True).start()
    app.run(port =5000)




            