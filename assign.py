from flask import Flask
import requests
import pprint
r =requests.get('https://api.openweathermap.org/data/2.5/weather?q=Corvallis,us&APPID=0d4c3c05756767f0202df9dd82e9d402')
pprint.pprint(r.text)

app = Flask(__name__)

@app.route('/')
def hello_world():
    return r.text
 
# main driver function
if __name__ == '__main__':
 
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()