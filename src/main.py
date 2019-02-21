import os
import requests
import SimpleHTTPServer
import SocketServer

TOKEN = os.environ["TOKEN"]
SMARTMEX_HOST=os.environ["SMARTMEX_HOST"]
PORT = int(os.environ["PORT"])

def get_token_for_web():
    REQUEST_STRUCT={
    "token": TOKEN,
    "scope": "company",
    "subscribe": [
        "CallStarted",
        "CallConnected",
        "CallCompleted"]
    }
    SMARTMEX_API_URL="https://{smartmex_host}/api/session_keys/create".format(smartmex_host=SMARTMEX_HOST)
    r = requests.post(SMARTMEX_API_URL, json=REQUEST_STRUCT)
    web_token = r.json()['data']
    return web_token


def do_GET(self):
    self.send_response(200)
    self.end_headers()
    sr="""<html>

        <script>
            wssocket = new WebSocket("wss://{smartmex_host}/api/ws");
            wssocket.onopen = function (event) {
                wssocket.send(JSON.stringify({type: "AuthRequest", wss_token: "{wss_token}"}));
            };
            wssocket.onmessage = function (event) {
                console.log(event.data);
            }
        </script>
        <body><h1>Open the console, and perform a call to see event flow!</h1></body>

    </html>"""
    sr= sr.replace("{smartmex_host}",SMARTMEX_HOST)
    sr = sr.replace("{wss_token}",get_token_for_web())
    
    self.wfile.write(sr)
    


if __name__=="__main__":

    Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
    Handler.do_GET=do_GET
    httpd = SocketServer.TCPServer(("", PORT), Handler)
    print "serving at port", PORT
    httpd.serve_forever()
