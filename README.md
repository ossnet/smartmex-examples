# SMARTMEX WSS EVENT API USAGE EXAMPLE #

Files here demostrate how to set up browser event receive for Smartmex events through WebSocket.

## Prerequistes ##

1. You should have SmartMEX service activated for your company.
2. You should have at least one SMARTMEX POST JSON API token created with rights to access "/api/session_keys/create" endpoint.
3. You should be able to use this token from the machine you are running this example from.

Optional:
For ease of running the example, you should have  Docker and docker-compose installed.

## Running the example ##

### With docker-compose ###

1. git clone the project,
2. go to docker-compose.yml file and modify these lines according to your configuration:

```(yml)
      - TOKEN=QR3234872348723423423UIUY0
      - SMARTMEX_HOST=service.smartmex.eu
```

TOKEN - token genearted from SmartMEX selfcare;
SMARTMEX_HOST - hostname of the smartmex service - mobili-stotele.tele2.lt or zvanuparvaldnieks.lmt.lv

3. run docker-compose: ```$docker-compose up --build```
4. visit http://127.0.0.1:8000 in your browser, open console to see log and make a call

### With python ###

1. Install latest versions of python 3.X, and follwong python packages - requests, pyopenssl,service_identity, pycrypto
2. Export environment variables:

```(bash)
$export TOKEN=QR3234872348723423423UIUY0
$export SMARTMEX_HOST=service.smartmex.eu
$export PORT=8000
```

Where:
    TOKEN - token genearted from SmartMEX selfcare;
    SMARTMEX_HOST - hostname of the smartmex service - mobili-stotele.tele2.lt or zvanuparvaldnieks.lmt.lv
    PORT - local port service will listen on

3. Run example:

```(bash)
$cd src/
$python3 main3.py
```

## Principle of operation ##

The demonstrated example does following things:

1. On a new web page request, this python script requests new temporary token from SMARTMEX JSON POST API endpoint 
2. It includes this temporary token in a HTML document sent to browser
3. This temporary token is used by JavaScript to authenticate WebSocket session and start recieving events.
