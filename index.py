import datetime
import json
from kibana_object import KibanaObject
# "2018-06-11T11:02:00.525Z" old timezone

class Index(KibanaObject):
    def __init__(self, name):
        self.name = name
        self.id = None

    def callback(self, response):
        print(response.text)

    def get_name(self):
        return self.name + '*'

    def endpoint(self):
        return 'index-pattern:' + self.name

    def payload(self):
        hash = {
          "type": "index-pattern",
          "index-pattern": {
            "title": self.name + "*",
            "timeFieldName": "@timestamp",
          }
        }
        return hash

    def payload(self):
        hash = {
          "type": "index-pattern",
          "updated_at": self.current_time(),
          "index-pattern": {
            "title": self.name + "*",
            "timeFieldName": "@timestamp",
            "fields": self.__fields()
            }
        }
        return hash

    def __fields(self):
        hash = [
            {"name":"@timestamp","type":"date","count":0,"scripted":False,"searchable":True,"aggregatable":True,"readFromDocValues":True},
            {"name":"@version","type":"string","count":0,"scripted":False,"searchable":True,"aggregatable":True,"readFromDocValues":True},
            {"name":"_id","type":"string","count":0,"scripted":False,"searchable":True,"aggregatable":True,"readFromDocValues":False},
            {"name":"_index","type":"string","count":0,"scripted":False,"searchable":True,"aggregatable":True,"readFromDocValues":False},
            {"name":"_score","type":"number","count":0,"scripted":False,"searchable":False,"aggregatable":False,"readFromDocValues":False},
            {"name":"_source","type":"_source","count":0,"scripted":False,"searchable":False,"aggregatable":False,"readFromDocValues":False},
            {"name":"_type","type":"string","count":0,"scripted":False,"searchable":True,"aggregatable":True,"readFromDocValues":False},
            {"name":"geoip.ip","type":"ip","count":0,"scripted":False,"searchable":True,"aggregatable":True,"readFromDocValues":True},
            {"name":"geoip.latitude","type":"number","count":0,"scripted":False,"searchable":True,"aggregatable":True,"readFromDocValues":True},
            {"name":"geoip.location","type":"geo_point","count":0,"scripted":False,"searchable":True,"aggregatable":True,"readFromDocValues":True},
            {"name":"geoip.longitude","type":"number","count":0,"scripted":False,"searchable":True,"aggregatable":True,"readFromDocValues":True},
            {"name":"host","type":"string","count":0,"scripted":False,"searchable":True,"aggregatable":False,"readFromDocValues":False},
            {"name":"host.keyword","type":"string","count":0,"scripted":False,"searchable":True,"aggregatable":True,"readFromDocValues":True},
            {"name":"message","type":"string","count":0,"scripted":False,"searchable":True,"aggregatable":False,"readFromDocValues":False}
        ]
        return json.dumps(hash)
