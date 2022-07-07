#!/usr/bin/env python3

from ev3dev.ev3 import *
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse

motor_A = LargeMotor('outA')
motor_B = LargeMotor('outB')
motor_C = MediumMotor('outC')

def setSteering(steering):
    motor_C.run_to_abs_pos(position_sp=int(steering), speed_sp=500)

def setSpeed(speed):
    motor_A.run_forever(speed_sp=int(speed))
    motor_B.run_forever(speed_sp=-int(speed))

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        path = urlparse(self.path).path
        print(path)
        if (path == "/drive"):
          query = urlparse(self.path).query
          print(query)
          print(query.split("&"))
          query_components = dict(qc.split("=") for qc in query.split("&"))
          if ("speed" in query_components):
            setSpeed(query_components["speed"])
          if ("steering" in query_components):
            setSteering(query_components["steering"])
          self.send_response(200)
          self.end_headers()
          self.wfile.write(b'Speed set.')
        else:
          self.send_response(404)
          self.end_headers()
          self.wfile.write(b'Only handles requests to /drive.')


httpd = HTTPServer(('0.0.0.0', 80), SimpleHTTPRequestHandler)
httpd.serve_forever()

