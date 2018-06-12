import datetime
import json
from connection import Connection

class KibanaObject(Connection):

    def payload(self):
        return None

    def endpoint(self):
        return None

    def callback(self, response):
        print(response.text)
        return True

    def current_time(self):
        return datetime.datetime.now().isoformat()

    def save(self):
        print(self.endpoint())
        if self.endpoint():
            return self.make_request()
        else:
            raise AttributeError
