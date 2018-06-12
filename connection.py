import json
import requests

class Connection():
    def url(self):
        return 'http://localhost:9200/.kibana/doc/' + self.endpoint()

    def headers(self):
        return {'Content-Type': 'application/json'}

    def json_payload(self):
        return json.dumps(self.payload())

    def make_request(self):
        try:
            if self.payload():
                if self.id:
                    response = requests.put(self.url(), data=self.json_payload(), headers=self.headers())
                else:
                    response = requests.post(self.url(), data=self.json_payload(), headers=self.headers())
            else:
                response = requests.get(self.url())
            return self.handle_response(response)
        except requests.exceptions.RequestException as e:
            return self.handle_error(e)


    def handle_error(self, error):
        print(error)
        return False

    def handle_response(self, response):
        return self.callback(response)
