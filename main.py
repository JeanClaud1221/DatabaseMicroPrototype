from sqlGenerator import SqlGenerator
from enums import *
sl=SqlGenerator()
# res=sl.executeQuery(typeOfQuery.READ,"{\"name\":\"test\",\"fields\":[\"id\",\"name\"],\"values\":[\"t\",\"jckk\"]}")
filter_data = {
    "operator": "OR",
    "conditions": [
        {
            "operator": "AND",
            "conditions": [
                {"field": "age", "operator": ">", "value": 25},
                {"field": "salary", "operator": ">", "value": 50000}
            ]
        },
        {
            "operator": "AND", 
            "conditions": [
                {"field": "status", "operator": "=", "value": "active"},
                {"field": "department", "operator": "=", "value": "HR"}
            ]
        }
    ]
}
res=sl.executeQuery(typeOfQuery.READ,filter_data)
print(res)