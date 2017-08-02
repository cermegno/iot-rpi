import os
from flask import Flask
import redis

r = redis.Redis(host='127.0.0.1', port='6379')

r.set('RPIvalue','I can hear Redis loud and clear!!')

app = Flask(__name__)

@app.route('/')
def mainmenu():

    global r
    PIval = r.get('RPIvalue')

    return """
    <html>
    <body>

    <center><h1>Hi, I'm up<br/>
	<h2><u>The latest value RPi sent is: {0}<br>
    </center>
    </body>
    </html>
    """.format(PIval)

if __name__ == "__main__":
	app.run(debug=False,host='0.0.0.0', port=int(os.getenv('PORT', '5000')))
