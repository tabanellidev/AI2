from threading import Thread, Event
from time import sleep
from http.server import BaseHTTPRequestHandler, HTTPServer

hostname = "localhost"
serverPort = 8080

# create a new Event object
event = Event()

class Worker(Thread):
    def __init__(self, event, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.event = event

    def run(self) -> None:
        for i in range(10):
            print(f'Running #{i+1}')
            sleep(1)
            if self.event.is_set():
                print('The thread was stopped prematurely.')
                break
        else:
            print('The thread was stopped maturely.')


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
            print('Start the server')
            thread = Worker(event)
            thread.start()
            
            messagge = "Worker started"

        if line == 'stop':
            print('Stop the server')
            event.set()    

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
