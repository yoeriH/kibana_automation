from flask import Flask
from kibana_object import KibanaObject

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
