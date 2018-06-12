from kibana_object import KibanaObject
import datetime
import string
import random
import time

error_budget = 99

def id_generator(size=12, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


class DemoData(KibanaObject):
        def __init__(self, name):
            self.name = name
            self.id = id_generator()
            self.active = 0 if random.random() > 0.995 else 1

        def url(self):
            return 'http://localhost:9200/logstash-demo-data/doc/' + self.id

        def callback(self, response):
            print(response.text)

        def endpoint(self):
            return self.id

        def payload(self):
            hash = {
              "@timestamp": datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S.000Z'),
              "host": 'Yoeri',
              "error_budget": error_budget,
              "message": "application_1 " + str(self.active)
            }
            return hash

while True:
    data = DemoData('test')
    data.save()
    time.sleep(5)
