from sqlGenerator import SqlGenerator
from enums import *
import json
sl=SqlGenerator()
# res=sl.executeQuery(typeOfQuery.READ,"{\"name\":\"test\",\"fields\":[\"id\",\"name\"],\"values\":[\"t\",\"jckk\"]}")
request = {"name":"filter","columns":["name","surname"],"filters":{
        "field":"age","operator":"<","value":30
}}
sl.executeQuery(typeOfQuery.READ,json.dumps(request))