from flask import Flask;

app = Flask(__name__)

@app.route('/members')
def members():
    return{"members":["member1","member2","member3"]}


if __name__ == "__main__":
    app.run(debug=True)









#PS F:\flask-react-arpan\flask-server> type > server.py

# PS F:\flask-react-arpan\flask-server> python -m venv venv
# PS F:\flask-react-arpan\flask-server> venv\Scripts\activate
# (venv) PS F:\flask-react-arpan\flask-server> 

# (venv) PS F:\flask-react-arpan\flask-server> pip install flask

# (venv) PS F:\flask-react-arpan\flask-server> python server.py
#  * Serving Flask app 'server' (lazy loading)
#  * Environment: production
#    WARNING: This is a development server. Do not use it in a production deployment.
#    Use a production WSGI server instead.       
#  * Debug mode: on
#  * Restarting with stat
#  * Debugger is active!
#  * Debugger PIN: 299-692-780
#  * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)