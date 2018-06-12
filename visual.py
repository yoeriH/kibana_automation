import datetime
import json
from kibana_object import KibanaObject

class Visual(KibanaObject):
    def __init__(self, name, index):
        self.name = name
        self.index = index
        self.id = None

    def payload(self):
        hash = {
          "type": "visualization",
          "updated_at": self.current_time(),
          "visualization": {
            "title": self.name,
            "visState": json.dumps(self.visual()),
            "uiStateJSON": "{}",
            "description": "",
            "version": 1,
            "kibanaSavedObjectMeta": {
              "searchSourceJSON": "{}"
            }
          }
        }
        return hash

    def endpoint(self):
        return 'visualization:' + self.name

    def visual(self):
        hash =  {
            "title":"timeline",
            "type":"metrics",
            "params": {
                "id": self.name,
                "type":"timeseries",
                "series":[{
                    "id":"61ca57f1-469d-11e7-af02-69e470af7417",
                    "color":"#68BC00",
                    "split_mode":"filter",
                    "metrics":[{
                        # "id":"61ca57f2-469d-11e7-af02-69e470af7417",
                        "type":"count"
                    }],
                    "seperate_axis":0,
                    "axis_position":"right",
                    "formatter":"number",
                    "chart_type":"line",
                    "line_width":1,
                    "point_size":1,
                    "fill":0.5,
                    "stacked":"none",
                    "split_filters":[{
                        "color":"#68BC00",
                        # "id":"bc623c80-6d86-11e8-9932-7df10f2512d3"
                    }],
                    "label":"",
                    "filter":"app*"
                }],
                "time_field":"@timestamp",
                "index_pattern": self.index.get_name(),
                "interval":"auto",
                "axis_position":"left",
                "axis_formatter":"number",
                "show_legend":1,
                "show_grid":1,
                # "background_color_rules":[{"id":"cda57ca0-6d86-11e8-9932-7df10f2512d3"}],
                # "bar_color_rules":[{"id":"ce593c40-6d86-11e8-9932-7df10f2512d3"}],
                # "gauge_color_rules":[{"id":"d031f3e0-6d86-11e8-9932-7df10f2512d3"}],
                "gauge_width":10,
                "gauge_inner_width":10,
                "gauge_style":"half"
            },
            "aggs":[]
        }
        return hash
