from threading import Thread, Event
from time import sleep
from http.server import BaseHTTPRequestHandler, HTTPServer

import pyautogui
import pydirectinput
import time 
import pygetwindow
from pygetwindow import PyGetWindowException

hostname = "192.168.56.1"
serverPort = 8080



# create a new Event object
event = Event()

class Worker(Thread):
    def __init__(self, event, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.event = event

    def run(self) -> None:

        
        

        while True:
            w = pygetwindow.getWindowsWithTitle('METIN2')[0]
            w.activate()
            pydirectinput.press('1',1)
            pydirectinput.press('z',4)
            w1 = pygetwindow.getWindowsWithTitle('METIN2')[1]
            w1.activate()
            pydirectinput.press('1',1)
            pydirectinput.press('z',4)

            if self.event.is_set():
                print('Workers Terminated.')
                break


class Server(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type","text/html")
        self.end_headers()

        message = "Hello, World! Here is GET response"
        self.wfile.write(bytes(message, "utf8"))

    def do_POST(self):

        self.send_response(200)
        self.send_header("Content-type","text/html")
        self.end_headers()
        
        content_length = int(self.headers['Content-Length'])
        file_content = self.rfile.read(content_length)
        line = file_content.decode('utf-8')

        #Messagge sent
        print(line)

        if line == 'start':
            print('Starting Workers')
            thread = Worker(event)
            thread.start()
            
            messagge = "Workers started"

        if line == 'stop':
            print('Stopping Workers')
            event.set()    
            sleep(3)
            event.clear()
            print('Workers ready again')
            messagge = "Worker stopped"

            


        self.wfile.write(bytes(messagge,"utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer((hostname,serverPort),Server)
    print("Server started http://%s:%s" % (hostname, serverPort))

    try:
      webServer.serve_forever()
    except KeyboardInterrupt:
      pass

    webServer.server_close()
    print("\nServer stopped")


