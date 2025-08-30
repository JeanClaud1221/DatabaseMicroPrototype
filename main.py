from sqlGenerator import SqlGenerator
from enums import *
sl=SqlGenerator()
res=sl.executeQuery(typeOfQuery.INSERT,"{\"name\":\"test\",\"fields\":[\"id\",\"name\"],\"values\":[1,\"jc\"]}")
